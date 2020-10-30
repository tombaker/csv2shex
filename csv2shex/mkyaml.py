"""Generate intermediate YAML expression from CSV file."""


import sys
from ruamel.yaml import YAML
from .csvreader import csvreader
from .csvrows import list_statements
from .mkshapes import list_shapes, Shape


def shapes2yaml(shapes_list):
    """Print YAML string to console from list of Shape objects."""
    yml = YAML()
    yml.register_class(Shape)
    yml.dump(shapes_list, sys.stdout)


def csv2yaml(csvfile):
    """Print YAML string to console from CSV file."""
    statements = list_statements(csvreader(csvfile))
    shapes = list_shapes(statements)
    return shapes2yaml(shapes)
