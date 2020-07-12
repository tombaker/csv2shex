"""Class for Python objects derived from CSV files."""


import csv
from dataclasses import dataclass
from pathlib import Path

# pylint: disable=no-self-use,too-many-branches
# => self-use: for now...
# => too-many-branches: a matter of taste?

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
        # self._property_id_is_mandatory()
        # self._value_type_is_valid_type()
        return True


def csvreader(csvfile):
    """Open CSV file and return csv.DictReader object as list."""
    rows_odict = csv.DictReader(Path(csvfile).open(newline="", encoding="utf-8-sig"))
    rows = [dict(r) for r in rows_odict]
    return rows


def list_statements(csvrow_list=None):
    """Return list of Statement objects from csv.DictReader object."""
    statements_list = []
    shape_ids = []
    first_shape_encountered = True
    for row in csvrow_list:
        if not row["prop_id"]:
            if row["shape_id"]:
                shape_ids.append(row["shape_id"])
            continue

        stat = Statement()
        stat.prop_id = row["prop_id"]
        stat.value_type = row["value_type"]

        if row["shape_id"]:
            stat.shape_id = row["shape_id"]
        else:
            if shape_ids:
                stat.shape_id = shape_ids[-1]
            elif not shape_ids:
                stat.shape_id = "@default"
        if stat.shape_id not in shape_ids:
            shape_ids.append(stat.shape_id)
        if first_shape_encountered:
            first_shape = stat.shape_id
            first_shape_encountered = False
        if stat.shape_id == first_shape:
            stat.start = True

        statements_list.append(stat)
    return statements_list
