"""Config constants. Write and read configuration file."""

import os
from pathlib import Path
import ruamel.yaml
from .exceptions import ConfigWarning, BadYamlError

# pylint: disable=bad-continuation
# => black disagrees

CSV_ELEMENTS = """\
shape_elements:
- shapeID
- shapeLabel
- shapeClosed
- start

statement_elements:
- propertyID
- propertyLabel
- mandatory
- repeatable
- valueNodeType
- valueDataType
- valueConstraint
- valueConstraintType
- valueShape
- note
"""

CONFIGFILE_NAME = ".csv2rc"

CONFIG_DEFAULTS = """\
prefixes:
    : http://example.org/
    dc: http://purl.org/dc/elements/1.1/
    dcat: http://www.w3.org/ns/dcat
    dct: http://purl.org/dc/terms/
    dcterms: http://purl.org/dc/terms/
    foaf: http://xmlns.com/foaf/0.1/
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    rdfs: http://www.w3.org/2000/01/rdf-schema#
    skos: http://www.w3.org/2004/02/skos/core#
    skosxl: http://www.w3.org/2008/05/skos-xl#
    sx: http://www.w3.org/ns/shex
    xsd: http://www.w3.org/2001/XMLSchema#
    wd: https://www.wikidata.org/wiki/
    wdt: http://www.wikidata.org/prop/direct/

valueNodeType:
- URI
- BNode
- Literal
- Nonliteral

valueConstraintType:
- Datatype
- UriStem
- UriPicklist
- LitPicklist
- LangTag
- LangTagPicklist
- Regex
"""

def writer_starter_configfile(
    rootdir=None, configfile_name=CONFIGFILE_NAME, config_defaults=CONFIG_DEFAULTS, 
):
    """Write initial config file (prefixes.yml) if not yet exists."""
    if not rootdir:
        rootdir = Path.cwd()
    file_tobewritten_pathname = Path(rootdir) / configfile_name
    if not os.path.exists(file_tobewritten_pathname):
        with open(file_tobewritten_pathname, "w", encoding="utf-8") as outfile:
            print(f"Writing {configfile_name}")
            outfile.write(config_content)


def get_prefixes(rootdir=None, configfile_name=CONFIGFILE_NAME, config_defaults=CONFIG_DEFAULTS):
    """Returns config dictionary from YAML config file (or errors out)."""
    if not rootdir:
        rootdir = Path.cwd()
    configfile_pathname = Path(rootdir) / configfile_name

    try:
        configfile_contents = Path(configfile_pathname).read_text()
    except FileNotFoundError:
        raise ConfigWarning(f"Optional config file {repr(configfile_name)} not found - skipping.")

    try:
        return ruamel.yaml.safe_load(configfile_contents)
    except ruamel.yaml.YAMLError:
        raise BadYamlError(f"Ignoring badly formed config file {repr(configfile_name)} - using built-in defaults. Fix!")
        return ruamel.yaml.safe_load(CONFIG_DEFAULTS)
