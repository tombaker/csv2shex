"""Write and read configuration file."""


import datetime
import os
from pathlib import Path
import ruamel.yaml
from .exceptions import ConfigWarning, BadYamlError

# pylint: disable=bad-continuation
# => black disagrees

CONFIGFILE_NAME = "csv2shex.yml"
CONFIGFILE_CONTENT = (
    "prefixes:\n"
    "    dc: http://purl.org/dc/elements/1.1/\n"
    "    dcterms: http://purl.org/dc/terms/\n"
    "    dct: http://purl.org/dc/terms/\n"
    "    foaf: http://xmlns.com/foaf/0.1/\n"
    "    skos: http://www.w3.org/2004/02/skos/core#\n"
    "    skosxl: http://www.w3.org/2008/05/skos-xl#\n"
)


def write_starter_configfile(
    rootdir=None, configfile=CONFIGFILE_NAME, config_content=CONFIGFILE_CONTENT
):
    """Write initial config file (csv2shex.yml) to current directory."""
    if not rootdir:
        rootdir = Path.cwd()
    file_tobewritten_pathname = Path(rootdir) / configfile
    if os.path.exists(file_tobewritten_pathname):
        raise ConfigWarning(f"Config file already initialized.")
    with open(file_tobewritten_pathname, "w", encoding="utf-8") as outfile:
        outfile.write(config_content)


def get_configdict(rootdir=None, configfile=CONFIGFILE_NAME):
    """Returns config dictionary from YAML config file (or errors out)."""
    if not rootdir:
        rootdir = Path.cwd()
    configfile = Path(rootdir) / configfile
    try:
        configfile_contents = Path(configfile).read_text()
    except FileNotFoundError:
        raise ConfigWarning(f"Config file {repr(configfile)} not found.")
    try:
        return ruamel.yaml.safe_load(configfile_contents)
    except ruamel.yaml.YAMLError:
        raise BadYamlError(f"YAML in {repr(configfile)} does not parse.")
