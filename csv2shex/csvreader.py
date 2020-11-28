"""Read DCAP/CSV (expand prefixes?). Write and read config file."""

from csv import DictReader
from dataclasses import asdict
from typing import Dict, List
from pathlib import Path
from csv2shex.exceptions import CsvError
from .csvshape import CSVShape, CSVTripleConstraint

DEFAULT_SHAPE=":default"
csvshape_keys = list(asdict(CSVShape()).keys())
csvshape_keys.remove('tc_list')
CSVSHAPE_ELEMENTS = csvshape_keys
TC_ELEMENTS = list(asdict(CSVTripleConstraint()).keys())

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

    shapes_dict: Dict[str, CSVShape] = dict()        # To make dict indexing CSVShapes,
    first_valid_row_encountered = True               # read CSV rows as list of dicts.

    for row in rows:                                 # For each row,
        if not row["propertyID"]:                    # where no propertyID is found,
            continue                                 # skip the row and move to next.

        if row["shapeID"]:                           # If true shapeID is found in row,
            sh_id = row["shapeID"]                   # use it as shape_dicts key, and
            shapes_dict[sh_id] = CSVShape()          # assign to it a new CSVShape.
        else:                                        # If false shapeID is found,
            if first_valid_row_encountered:          # in first valid row encountered,
                row["shapeID"] = sh_id = ":default"  # use ':default' as dict key, and
                shapes_dict[sh_id] = CSVShape()      # assign to it a new CSVShape.
            else:                                    # but in any row thereafter,
                so_far = [k for k in shapes_dict]    # list shapeIDs used so far, and
                sh_id = so_far[-1]                   # use the latest one.

        if first_valid_row_encountered:              # First shape encountered is
            shapes_dict[sh_id].start = True          # marked as "start" shape, but
            first_valid_row_encountered = False      # only the first.

        shape = shapes_dict[sh_id]                   # Call current shape "shape",
        for elem in CSVSHAPE_ELEMENTS:               # iterate shape-related elements,
            try:                                     # populate csvshape attributes,
                setattr(shape, elem, row[elem])      # with values from row dict,
            except KeyError:                         # while missing elements,
                pass                                 # are skipped.

        tc = CSVTripleConstraint()                   # Make triple constraint object.
        for elem in TC_ELEMENTS:                     # Iterating tc-related elements,
            try:                                     # populate tc-object attributes,
                setattr(tc, elem, row[elem])         # with values from row dict,
            except KeyError:                         # while missing elements,
                pass                                 # are skipped.

        shapes_dict[sh_id].tc_list.append(tc)        # Append TC to shapes dict.

    return list(shapes_dict.values())                # Return list of shapes.
