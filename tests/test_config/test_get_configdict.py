"""Return config dictionary from reading config file."""

import os
import pytest
from pathlib import Path
from csv2shex.config import CONFIGFILE_NAME, get_config_settings

# def get_config_settings(
#     rootdir_path=None, 
#     configfile_name=CONFIGFILE_NAME, 
#     config_defaults=CONFIG_DEFAULTS, 
#     verbose=False
# ):


def test_get_config_settings_dict_prefixes(dir_with_csv2rc):
    """Return dictionary of configuration settings from config file .csvrc."""
    os.chdir(Path(dir_with_csv2rc))
    assert get_config_settings()["prefixes"] == {':': 'http://example.org/', 'dct:': 'http://purl.org/dc/terms/'}


@pytest.mark.skip
def test_get_config_settings_from_configfile_with_lines_commented_out(dir_with_csv2rc):
    """Return configuration dictionary even if some lines are commented out."""
    os.chdir(tmp_path)
    print(get_config_settings()["prefixes"])
    configfile_content = "verbose: False\n" "# htmlify: True\n"
    Path(CONFIGFILE_NAME).write_text(configfile_content)
    expected = {"verbose": False}
    assert get_config_settings() == expected


@pytest.mark.skip
def test_exit_if_configfile_not_found(tmp_path):
    """Raise exception if no configuration YAML file is found."""
    os.chdir(tmp_path)
    with pytest.raises(SystemExit):
        get_config_settings()


@pytest.mark.skip
def test_exit_if_configfile_not_found_when_rootdir_explicitly_specified(tmp_path):
    """Raise exception if no config file found when explicitly specifying rootdir."""
    os.chdir(tmp_path)
    cwd = Path.cwd()
    with pytest.raises(SystemExit):
        get_config_settings(rootdir_path=cwd)


def test_exit_if_configfile_has_bad_yaml(tmp_path):
    """Raise exception if config file has bad YAML."""
    os.chdir(tmp_path)
    configfile_content = "DELIBE\nRATELY BAD: -: ^^YAML CONTENT^^\n"
    Path(CONFIGFILE_NAME).write_text(configfile_content)
    with pytest.raises(SystemExit):
        get_config_settings()
