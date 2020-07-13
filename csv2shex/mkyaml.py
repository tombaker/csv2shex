"""Generate intermediate YAML expression from list of Shape objects."""


import sys
from ruamel.yaml import YAML
from .mkstatements import csvreader, list_statements
from .mkshapes import pprint_shapes, list_shapes, Shape


def csv2yaml(shapes_list):
    """Print YAML string to console from list of Shape objects."""
    yml = YAML()
    yml.register_class(Shape)
    yml.dump(shapes_list, sys.stdout)


