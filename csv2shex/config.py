"""Initialize config files."""

import os
from pathlib import Path
from warnings import warn
from .exceptions import ConfigWarning

SHAPE_KEYS = ["shape_id", "shape_label", "start"]

STATEMENT_KEYS = [
    "prop_id",
    "prop_label",
    "mand",
    "repeat",
    "value_type",
    "value_datatype",
    "constraint_value",
    "constraint_type",
    "shape_ref",
    "annot",
]

PREFIXFILE_NAME = "prefixes.yml"

PREFIXFILE_CONTENT = """\
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

CONFIGFILE_CONTENT = """\
invalid_filename_patterns:
- \.swp$
- \.tmp$
- ~$
#
# # maps files to destinations (paths are absolute or relative to repo root)
# files2dirs_dict:
#     to_a.txt: a
#     to_b.txt: b
#     to_c.txt: /Users/foo/logs
#
# # lists stems of pathnames to be linkified
# pathstem_list:
# - /Users/foobar
# - /home/foobar
"""

# def write_minimal_rulefiles(
#     rootdir_path=None,
#     datadir_name=DATADIR_NAME,
#     datadir_rulefile=DATADIR_RULEFILE_NAME,
#     datadir_rulefile_contents=DATADIR_RULEFILE_MINIMAL_CONTENTS,
#     root_rulefile=ROOTDIR_RULEFILE_NAME,
#     root_rulefile_contents=ROOTDIR_RULEFILE_CONTENTS,
# ):
#     """Write starter rule files to root directory and to starter data directory."""
#     # pylint: disable=too-many-arguments
#     if not rootdir_path:
#         rootdir_path = Path.cwd()
#     rootdir_rules = Path(root_rulefile)
#     datadir = Path(rootdir_path) / datadir_name
#     datadir.mkdir(parents=True, exist_ok=True)
#     datadir_rules = Path(datadir) / datadir_rulefile
#     if rootdir_rules.exists():
#         warn(f"Will use existing rule file {str(rootdir_rules)}.", ConfigWarning)
#     else:
#         rootdir_rules.write_text(root_rulefile_contents)
#     if datadir_rules.exists():
#         warn(f"Will use existing rule file {str(datadir_rules)}.", ConfigWarning)
#     else:
#         datadir_rules.write_text(datadir_rulefile_contents)


# def write_starter_configfile(
#     rootdir_path=None,
#     configfile_name=CONFIGFILE_NAME,
#     configfile_content=CONFIGFILE_CONTENT,
# ):
#     """Write initial config file (mklists.yml) to root directory."""
#     if not rootdir_path:
#         rootdir_path = Path.cwd()
#     file_tobewritten_pathname = Path(rootdir_path) / configfile_name
#     if os.path.exists(file_tobewritten_pathname):
#         raise MklistsError(f"Repo already initialized.")
#     with open(file_tobewritten_pathname, "w", encoding="utf-8") as outfile:
#         outfile.write(configfile_content)

