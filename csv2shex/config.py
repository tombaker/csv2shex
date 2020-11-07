"""Config constants. Write and read configuration file."""

import os
from pathlib import Path
import ruamel.yaml as yaml
from .defaults import DEFAULT_CONFIGFILE_NAME, DEFAULT_CONFIG_SETTINGS_YAML
from .exceptions import ConfigError
from .readwrite import get_config_settings_dict

CONFIG_SETTINGS_DICT = readwrite.get_config_settings_dict()
