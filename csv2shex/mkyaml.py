"""Generate intermediate YAML expression from CSV file."""


import sys
from ruamel.yaml import YAML
from .csvreader import csvreader
from .csvrows import list_statements
from .csvshapes import list_csvshapes, CSVShape


def shapes2yaml(shapes_list):
    """Print YAML string to console from list of CSVShape objects."""
    yml = YAML()
    yml.register_class(CSVShape)
    yml.dump(shapes_list, sys.stdout)


def csv2yaml(csvfile):
    """Print YAML string to console from CSV file."""
    statements = list_statements(csvreader(csvfile))
    shapes = list_csvshapes(statements)
    return shapes2yaml(shapes)
