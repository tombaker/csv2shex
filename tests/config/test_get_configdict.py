"""Return config dictionary from reading config file."""

import os
import pytest
from pathlib import Path
from csv2shex.config import CONFIGFILE_NAME, get_configdict

CONFIGFILE_CONTENT = (
    "prefixes:\n"
    "    dc: http://purl.org/dc/elements/1.1/\n"
    "    dcterms: http://purl.org/dc/terms/\n"
)

CONFIG_PYOBJ = {
    "prefixes": {
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
    }
}


def test_get_configdict(tmp_path):
    """Return dictionary of configuration settings from YAML file."""
    os.chdir(tmp_path)
    Path(CONFIGFILE_NAME).write_text(CONFIGFILE_CONTENT)
    assert get_configdict() == CONFIG_PYOBJ


def test_get_configdict_from_configfile_with_lines_commented_out(tmp_path):
    """Return configuration dictionary even if some lines are commented out."""
    os.chdir(tmp_path)
    configfile_content = (
        "prefixes:\n"
        "#   dc: http://purl.org/dc/elements/1.1/\n"
        "    dcterms: http://purl.org/dc/terms/\n"
    )
    Path(CONFIGFILE_NAME).write_text(configfile_content)
    expected = {"prefixes": {"dcterms": "http://purl.org/dc/terms/"}}
    assert get_configdict() == expected


def test_exit_if_configfile_has_bad_yaml(tmp_path):
    """Raise exception if config file has bad YAML."""
    os.chdir(tmp_path)
    configfile_content = "DELIBE\nRATELY BAD: -: ^^YAML CONTENT^^\n"
    Path(CONFIGFILE_NAME).write_text(configfile_content)
    with pytest.raises(SystemExit):
        get_configdict()
