"""Class for Python objects derived from CSV files."""


import csv
from dataclasses import dataclass
from .exceptions import StatementError


@dataclass
class Statement:
    """Holds state and self-validation methods for a statement."""

    start: bool = False
    shape_id: str = None
    shape_label: str = None
    prop_id: str = None
    prop_label: str = None
    mand: str = None
    repeat: str = None
    value_type: str = None
    value_datatype: str = None
    constraint_value: str = None
    constraint_type: str = None
    shape_ref: str = None
    annot: str = None

    def is_valid(self):
        """Returns True if Statement instance is valid."""
        self._property_id_is_mandatory()
        self._value_type_is_valid_type()
        return True


def csvreader(csvfile):
    """Open CSV file and return csv.DictReader object as list."""
    list_of_odicts = csv.DictReader(open(csvfile, newline="", encoding="utf-8-sig"))
    list_of_dicts = [dict(r) for r in list_of_odicts]
    return list_of_dicts
#    return list(csv.DictReader(open(csvfile, newline="", encoding="utf-8-sig")))


def list_statements(csvreader=None):
    """Return list of Statement objects from csv.DictReader object."""
    statements_list = []
    shape_ids = []
    first_shape_encountered = True
    for row in csvreader:
        if not dict(row.items())["prop_id"]:
            if dict(row.items())["shape_id"]:
                shape_ids.append(dict(row.items())["shape_id"])
            continue
        stat = Statement()
        for (key, value) in row.items():
            if key == "prop_id":
                stat.prop_id = value
            if key == "shape_id":
                if value:
                    stat.shape_id = value
                else:
                    if shape_ids:
                        stat.shape_id = shape_ids[-1]
                    elif not shape_ids:
                        stat.shape_id = "@default"
                if stat.shape_id not in shape_ids:
                    shape_ids.append(stat.shape_id)
                if first_shape_encountered:
                    stat.start = True
                    first_shape = stat.shape_id
                    first_shape_encountered = False
                if stat.shape_id == first_shape:
                    stat.start = True
            if key == "value_type":
                stat.value_type = value
        statements_list.append(stat)
    return statements_list
