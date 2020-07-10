"""Class for Python objects derived from CSV files."""


import csv
from dataclasses import dataclass
from .exceptions import StatementError


@dataclass
class Statement:
    """Holds state and self-validation methods for a statement."""

    start: bool = False
    shapeid: str = None
    prop_id: str = None
    v_type: str = None
    shape_ref: str = None

    def is_valid(self):
        """Returns True if Statement instance is valid."""
        self._property_id_is_mandatory()
        self._v_type_is_valid_type()
        return True


def csvreader(csvfile):
    """Open CSV file and return csv.DictReader object as list."""
    return list(csv.DictReader(open(csvfile, newline="", encoding="utf-8-sig")))


def list_statements(csvreader=None):
    """Return list of Statement objects from csv.DictReader object."""
    statements_list = []
    shapeids = []
    for row in csvreader:
        if not dict(row.items())["prop_id"]:
            if dict(row.items())["shapeid"]:
                shapeids.append(dict(row.items())["shapeid"])
            continue
        stat = Statement()
        for (key, value) in row.items():
            if key == "prop_id":
                stat.prop_id = value
            if key == "shapeid":
                if value:
                    stat.shapeid = value
                else:
                    if shapeids:
                        stat.shapeid = shapeids[-1]
                    elif not shapeids:
                        stat.shapeid = "@default"
            if key == "v_type":
                stat.v_type = value
            if stat.shapeid not in shapeids:
                shapeids.append(stat.shapeid)
        statements_list.append(stat)
    return statements_list
