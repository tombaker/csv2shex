"""Return config dictionary from reading config file."""

import os
import pytest
from pathlib import Path
from csv2shex.defaults import DEFAULT_CONFIGFILE_NAME
from csv2shex.exceptions import BadYamlError, ConfigWarning
from csv2shex.readwrite import get_config_settings_dict


ALT_CONFIG_SETTINGS_YAML = """\
prefixes:
    ":": "http://example.org/"
    "dcterms:": "http://purl.org/dc/terms/"
"""


def test_get_config_settings_dict_dict_from_default_config_file(dir_with_csv2rc):
    """Return dictionary of configuration settings from config file .csvrc."""
    os.chdir(Path(dir_with_csv2rc))
    assert get_config_settings_dict()["prefixes"] == {
        ":": "http://example.org/",
        "dct:": "http://purl.org/dc/terms/",
    }
    assert get_config_settings_dict() == {
        "prefixes": {":": "http://example.org/", "dct:": "http://purl.org/dc/terms/"},
        "valueNodeType": ["URI", "BNode", "Nonliteral"],
        "valueConstraintType": ["UriStem", "LitPicklist"],
    }


def test_get_default_config_settings_if_configfile_not_found(tmp_path):
    """Get default config settings if no default config file is found."""
    os.chdir(tmp_path)
    assert get_config_settings_dict(default_config_settings_yaml=ALT_CONFIG_SETTINGS_YAML)[
        "prefixes"
    ] == {
        ":": "http://example.org/",
        "dcterms:": "http://purl.org/dc/terms/",
    }


def test_exit_if_configfile_has_bad_yaml(tmp_path):
    """Raise exception if config file has bad YAML."""
    os.chdir(tmp_path)
    configfile_content = "DELIBE\nRATELY BAD: -: ^^YAML CONTENT^^\n"
    Path(DEFAULT_CONFIGFILE_NAME).write_text(configfile_content)
    assert get_config_settings_dict(default_config_settings_yaml=ALT_CONFIG_SETTINGS_YAML)[
        "prefixes"
    ] == {
        ":": "http://example.org/",
        "dcterms:": "http://purl.org/dc/terms/",
    }
    # with pytest.raises(ConfigWarning):
    #    get_config_settings_dict()
