"""Read DCAP/CSV. Write and read config file."""

import os
import csv
from pathlib import Path
import ruamel.yaml as yaml
from .defaults import DEFAULT_CONFIGFILE_NAME, DEFAULT_CONFIG_SETTINGS_YAML
from .exceptions import CsvError, ConfigError


def csvreader(csvfile):
    """Read CSV file and return list of dicts, one dict per CSV row."""
    csv_dictreader_obj = csv.DictReader(
        Path(csvfile).open(newline="", encoding="utf-8-sig")
    )
    csvrow_dicts_list = list(csv_dictreader_obj)
    if "propertyID" not in list(csvrow_dicts_list[0].keys()):
        raise CsvError("To be valid, DCAP CSV must have a 'propertyID' column header.")
    return csvrow_dicts_list


def write_starter_configfile(
    basedir=None,
    default_configfile_name=DEFAULT_CONFIGFILE_NAME,
    default_config_settings_yaml=DEFAULT_CONFIG_SETTINGS_YAML,
):
    """Write initial config file, by default to CWD, or exit if already exists."""
    if not basedir:
        basedir = Path.cwd()
    configfile_pathname = Path(basedir) / default_configfile_name
    if os.path.exists(configfile_pathname):
        raise ConfigError(
            f"Found existing {str(configfile_pathname)} - delete to re-generate."
        )
    with open(configfile_pathname, "w", encoding="utf-8") as outfile:
        outfile.write(default_config_settings_yaml)
        print(f"Wrote config defaults (for editing) to: {str(configfile_pathname)}")


def get_config_settings_dict(
    rootdir_path=None,
    default_configfile_name=DEFAULT_CONFIGFILE_NAME,
    default_config_settings_yaml=DEFAULT_CONFIG_SETTINGS_YAML,
    verbose=False,
):
    """Returns config dict from config file, if found, or from built-in defaults."""
    if not rootdir_path:
        rootdir_path = Path.cwd()
    configfile_pathname = Path(rootdir_path) / default_configfile_name

    try:
        configfile_contents = Path(configfile_pathname).read_text()
        if verbose:
            print(f"Reading config file {repr(configfile_pathname)}.")
        return yaml.safe_load(configfile_contents)
    except FileNotFoundError:
        if verbose:
            print(
                f"Config file {repr(configfile_pathname)} not found - using defaults."
            )
        return yaml.safe_load(default_config_settings_yaml)
    except (yaml.YAMLError, yaml.scanner.ScannerError):
        print(
            f"Ignoring badly formed config file {repr(default_configfile_name)}"
            " - using defaults."
        )
        return yaml.safe_load(default_config_settings_yaml)


