"""Class for Python objects derived from CSV files."""

import csv
import os
import re
from collections import OrderedDict
from dataclasses import dataclass, asdict
from pathlib import Path
from .exceptions import StatementError


def list_shapes(statements_list):
    """@@@Docstring"""
    shapes = []
    shape_ids = []
#            if not shape_ids:
#                stat.start = True
    for statement in statements_list:
        if statement.shape_id not in shapes:
            shapes.append(statement)
#            if stat.shape_id not in shape_ids:
#                shape_ids.append(stat.shape_id)
    print(shapes)
    return shapes


def list_statements(csvreader=None):
    """Return list of statements from csv.DictReader object."""
    statements_list = []
    shape_ids = []
    for row in csvreader:
        stat = Statement()
        for (key, value) in row.items():
            if key == "shape_id":
                if value:
                    # print(f"stat.shape_id = {value}:")
                    stat.shape_id = value
                # print(f"elif not {value}:")
                else:
                    if shape_ids:
                        stat.shape_id = shape_ids[-1]
                    elif not shape_ids:
                        stat.shape_id = '@default'
            if key == "prop_id":
                stat.prop_id = value
            if key == "value_type":
                stat.value_type = value
            if stat.shape_id not in shape_ids:
                shape_ids.append(stat.shape_id)
        statements_list.append(stat)
    return statements_list


def csvreader(csvfile):
    """Open CSV file and return csv.DictReader object as list."""
    return list(csv.DictReader(open(csvfile, newline="", encoding="utf-8-sig")))


@dataclass
class Shape:
    """Holds state and self-validation methods for a shape."""


@dataclass
class Statement:
    """Holds state and self-validation methods for a statement."""

    start: str = False
    shape_id: str = None
    prop_id: str = None
    value_type: str = None

    def is_valid(self):
        """Returns True if Statement instance is valid."""
        self._property_id_is_mandatory()
        self._value_type_is_valid_type()
        return True
