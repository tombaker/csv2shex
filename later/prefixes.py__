"""Write and read configuration file."""


import os
from pathlib import Path
import ruamel.yaml
from .config import PREFIXFILE_NAME, PREFIXFILE_CONTENT
from .exceptions import ConfigWarning, BadYamlError

# pylint: disable=bad-continuation
# => black disagrees


def write_starter_prefixfile(
    rootdir=None, prefixfile=PREFIXFILE_NAME, config_content=PREFIXFILE_CONTENT
):
    """Write initial config file (prefixes.yml) if not yet exists."""
    if not rootdir:
        rootdir = Path.cwd()
    file_tobewritten_pathname = Path(rootdir) / prefixfile
    if not os.path.exists(file_tobewritten_pathname):
        with open(file_tobewritten_pathname, "w", encoding="utf-8") as outfile:
            print(f"Writing {prefixfile}")
            outfile.write(config_content)


def get_prefixes(rootdir=None, prefixfile=PREFIXFILE_NAME):
    """Returns config dictionary from YAML config file (or errors out)."""
    if not rootdir:
        rootdir = Path.cwd()
    prefixfile = Path(rootdir) / prefixfile
    try:
        prefixfile_contents = Path(prefixfile).read_text()
    except FileNotFoundError:
        raise ConfigWarning(f"Config file {repr(prefixfile)} not found.")
    try:
        return ruamel.yaml.safe_load(prefixfile_contents)
    except ruamel.yaml.YAMLError:
        raise BadYamlError(f"YAML in {repr(prefixfile)} does not parse.")
