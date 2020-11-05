"""Return config dictionary from reading config file."""

import os
import pytest
from pathlib import Path
from csv2shex.config import DEFAULT_CONFIGFILE_NAME, get_config_settings
from csv2shex.exceptions import BadYamlError, ConfigWarning

# def get_config_settings(
#     rootdir_path=None,
#     default_configfile_name=DEFAULT_CONFIGFILE_NAME,
#     config_defaults=CONFIG_DEFAULTS,
#     verbose=False
# ):

ALT_CONFIG_DEFAULTS = """\
prefixes:
    ":": "http://example.org/"
    "dc:": "http://purl.org/dc/elements/1.1/"
"""


def test_get_config_settings_dict_from_default_config_file(dir_with_csv2rc):
    """Return dictionary of configuration settings from config file .csvrc."""
    os.chdir(Path(dir_with_csv2rc))
    assert get_config_settings()["prefixes"] == {
        ":": "http://example.org/",
        "dct:": "http://purl.org/dc/terms/",
    }


def test_get_default_config_settings_if_configfile_not_found(tmp_path):
    """Get default config settings if no default config file is found."""
    os.chdir(tmp_path)
    assert get_config_settings(config_defaults=ALT_CONFIG_DEFAULTS)["prefixes"] == {
        ":": "http://example.org/",
        "dc:": "http://purl.org/dc/elements/1.1/",
    }


def test_exit_if_configfile_has_bad_yaml(tmp_path):
    """Raise exception if config file has bad YAML."""
    os.chdir(tmp_path)
    configfile_content = "DELIBE\nRATELY BAD: -: ^^YAML CONTENT^^\n"
    Path(DEFAULT_CONFIGFILE_NAME).write_text(configfile_content)
    assert get_config_settings(config_defaults=ALT_CONFIG_DEFAULTS)["prefixes"] == {
        ":": "http://example.org/",
        "dc:": "http://purl.org/dc/elements/1.1/",
    }
    # with pytest.raises(ConfigWarning):
    #    get_config_settings()
