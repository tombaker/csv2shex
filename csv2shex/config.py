"""Initialize config files."""

import os
from pathlib import Path
# from warnings import warn
# import ruamel.yaml as yaml
from .exceptions import ConfigWarning

CONFIGFILE_NAME = ".c2src"

CONFIG_DEFAULTS = """\
shape_elements:
- shape_id
- shape_label
- start
statement_elements:
- prop_id
- prop_label
- mand
- repeat
- value_type
- value_datatype
- constraint_value
- constraint_type
- shape_ref
- annot
mandatory_repeatable_values:
- Y
- y
- N
- n
value_types:
- URI
- BNode
- Literal
- Nonliteral
constraint_type:
- URIStem
- Regex
- Date
prefixes:
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
    xsd: http://www.w3.org/2001/XMLSchema
"""


def write_configfile(
    configfile_name=CONFIGFILE_NAME,
    config_defaults=CONFIG_DEFAULTS,
):
    """Write initial config file to current directory."""
    file_tobewritten_pathname = Path(Path.cwd()) / configfile_name
    if os.path.exists(file_tobewritten_pathname):
        raise ConfigWarning("Repo already initialized.")
    with open(file_tobewritten_pathname, "w", encoding="utf-8") as outfile:
        outfile.write(config_defaults)

# return ruamel.yaml.safe_load(prefixfile_contents)
# except ruamel.yaml.YAMLError:
