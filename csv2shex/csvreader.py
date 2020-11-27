"""Read DCAP/CSV (expand prefixes?). Write and read config file."""

from csv import DictReader
from typing import Dict, List
from pathlib import Path
from csv2shex.exceptions import CsvError
from csv2shex.csvshape import CSVSHAPE_ELEMENTS, TC_ELEMENTS
from .csvshape import CSVShape, CSVTripleConstraint, CSVSchema


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


def _get_csvshapes(rows=None) -> List[CSVShape]:
    """Return list of CSVShape objects from list of row dicts."""
    # /Users/tbaker/github/tombaker/csv2shex/tests/test_get_csvshapes.py

    shapes_dict: Dict[str, CSVShape] = dict()       # To index CSVShape objects.
    first_valid_row_encountered = True

    for row in rows:                                # For each row in dict from CSV,
        if not row["propertyID"]:                   # if no propertyID found in row,
            continue                                # skip the row and move to next.

        if row["shapeID"]:                          # If non-empty shapeID found in row,
            id = row["shapeID"]                     # assign its value to 'id', and
        else:                                       # But if no shapeID is found, and
            if first_valid_row_encountered:         # if first valid row encountered,
                id = ":default"                     # assign ':default' to 'id', 
            else:                                   # tho with any row after first,
                so_far = list(shapes_dict.keys())   # list shapes created so far,
                id = so_far[-1]                     # and assign latest to 'id'.

        shapes_dict[id] = CSVShape()                # Use 'id' to index a new csvshape.

        if first_valid_row_encountered:             # In first valid row encountered,
            shapes_dict[id].start = True            # mark shape as "start" shape, and
            first_valid_row_encountered = False     # may no rows henceforth be "first".

        if id not in shapes_dict:                   # If ID has not been seen before,
            shapes_dict[id] = CSVShape()            # map new ID to new CSVShape object.

        shape = shapes_dict[id]                     # Current shape is called 'shape'.
        for elem in CSVSHAPE_ELEMENTS:              # Iterate shape-related elements,
            try:                                    # to populate its attributes,
                setattr(shape, elem, row[elem])     # with values from the row dict,
            except KeyError:                        # while any missing elements,
                pass                                # are skipped.

        tc = CSVTripleConstraint()                  # Make triple constraint object,
        for elem in TC_ELEMENTS:                    # iterate thru relevant elements,
            try:                                    # to populate its attributes,
                setattr(tc, elem, row[elem])        # with values from the row dict,
            except KeyError:                        # while any missing elements,
                pass                                # are skipped.

        shapes_dict[id].tc_list.append(tc)          # Append triple constraint.

    return list(shapes_dict.values())               # Return list of shapes.

