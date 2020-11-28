"""Read DCAP/CSV (expand prefixes?). Write and read config file."""

from csv import DictReader
from dataclasses import asdict
from typing import Dict, List
from pathlib import Path
from csv2shex.exceptions import CsvError
from .csvshape import CSVShape, CSVTripleConstraint

DEFAULT_SHAPE=":default"

def csvreader(csvfile):
    """Return list of CSVShape objects from CSV file."""
    rows = _get_rows(csvfile)
    csvshapes = _get_csvshapes(rows)
    return csvshapes


def _get_rows(csvfile):
    """Return list of row dicts from CSV file."""
    csv_dictreader = DictReader(Path(csvfile).open(newline="", encoding="utf-8-sig"))
    rows = list(csv_dictreader)
    if "propertyID" not in list(rows[0].keys()):
        raise CsvError("Valid DCAP CSV must have a 'propertyID' column.")
    return rows


def _get_csvshapes(rows=None, default_shape=DEFAULT_SHAPE) -> List[CSVShape]:
    """Return list of CSVShape objects from list of row dicts."""

    shapes: Dict[str, CSVShape] = dict()        # To make dict indexing CSVShapes,
    first_valid_row_encountered = True               # read CSV rows as list of dicts.

    def set_shape_fields(shape=None, row=None):
        """@@@"""
        csvshape_keys = list(asdict(CSVShape()))     # Get list of shape-related keys,
        #csvshape_keys.remove('shapeID')              # minus shapeID (see below), and
        csvshape_keys.remove('start')                # minus start (see below), and
        csvshape_keys.remove('tc_list')              # minus tc_list (see below).

        for key in csvshape_keys:                    # Iterate remaining shape keys, to
            try:                                     # populate csvshape attributes,
                setattr(shape, key, row[key])        # with values from the row dict,
            except KeyError:                         # while keys not used in dict,
                pass                                 # are simply skipped.

    for row in rows:                                 # For each row,
        if not row["propertyID"]:                    # where no propertyID is found,
            continue                                 # skip the row and move to next.

        if row["shapeID"]:                           # If true shapeID is found in row,
            sh_id = row["shapeID"]                   # use it as shape_dicts key, 
            shape = shapes[sh_id] = CSVShape()       # assign a new CSVShape and alias,
            set_shape_fields(shape, row)             # and set its shape-related fields.
        else:                                        # If false shapeID is found, and it
            if first_valid_row_encountered:          # is first valid row encountered,
                sh_id = ":default"                   # use ':default' as dict key, 
                shape = shapes[sh_id] = CSVShape()   # assign a new CSVShape and alias,
                set_shape_fields(shape, row)         # and set its shape-related fields.
            else:                                    # In other rows missing shapeIDs,
                so_far = [key for key in shapes]     # list shapeIDs used so far, 
                sh_id = so_far[-1]                   # and use latest one as the index
                shape = shapes[sh_id]                # for the current shape.

        if first_valid_row_encountered:              # First shape encountered is
            shapes[sh_id].start = True               # marked as "start" shape, but
            first_valid_row_encountered = False      # only the first.

        tc = CSVTripleConstraint()                   # Make a new TC object, and
        for key in list(asdict(tc)):                 # iterate TC-related keys, to
            try:                                     # populate that object,
                setattr(tc, key, row[key])           # with values from the row dict,
            except KeyError:                         # while keys not used in dict
                pass                                 # are simply skipped.

        shapes[sh_id].tc_list.append(tc)             # Append TC to csvshape in dict.

    return list(shapes.values())                     # Return list of shapes.
