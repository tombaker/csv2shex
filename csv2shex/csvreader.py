"""Read DCAP/CSV (expand prefixes?). Write and read config file."""

from csv import DictReader
from typing import Dict, List
from pathlib import Path
from csv2shex.exceptions import CsvError
from csv2shex.csvshape import CSVSHAPE_ELEMENTS, TC_ELEMENTS
from .csvshape import CSVShape, CSVTripleConstraint


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

    shapes_dict: Dict[str, CSVShape] = dict()       # To index CSVShape objects.
    first_valid_row_encountered = True

    for row in rows:                                # For each row in CSV dict,

        # Ignore non-valid lines (i.e.,
        if not row["propertyID"]:                   # if no propertyID found in row,
            continue                                # skip the row and move to next.

        # Determine key (sh_id) to be used for CSVShape instance as value in shapes_dict.
        if row["shapeID"]:                          # If non-empty shapeID found in row,
            sh_id = row["shapeID"]                  # assign to sh_id its value.
        else:                                       # But if no shapeID is found, and
            if first_valid_row_encountered:         # it is first valid row encountered,
                sh_id = ":default"                  # assign to sh_id the value ':default'.
            else:                                   # But in any row after the first,
                so_far = list(shapes_dict.keys())   # list shapes created so far and
                sh_id = so_far[-1]                  # assign to sh_id name of the latest.

        # Use key (sh_id) for new instance of CSVShape (value) in shapes_dict.
        shapes_dict[sh_id] = CSVShape()             # Add shape 'sh_id' to shapes_dict.

        # Mark first shape encountered as "start" shape.
        if first_valid_row_encountered:             # First row sets the first shape, so
            shapes_dict[sh_id].start = True         # mark it as "start" shape, and
            first_valid_row_encountered = False     # may no rows henceforth be "first".

        if sh_id not in shapes_dict:                # If 'sh_id' not seen before, map
            shapes_dict[sh_id] = CSVShape()         # new ID to new CSVShape object.

        shape = shapes_dict[sh_id]                  # Current shape is called "shape".
        for elem in CSVSHAPE_ELEMENTS:              # Iterating shape-related elements,
            try:                                    # populate shape-object attributes,
                setattr(shape, elem, row[elem])     # with values from row dict,
            except KeyError:                        # while missing elements,
                pass                                # are skipped.

        tc = CSVTripleConstraint()                  # Make triple constraint object.
        for elem in TC_ELEMENTS:                    # Iterating tc-related elements,
            try:                                    # populate tc-object attributes,
                setattr(tc, elem, row[elem])        # with values from row dict,
            except KeyError:                        # while missing elements,
                pass                                # are skipped.

        shapes_dict[sh_id].tc_list.append(tc)       # Append TC to shapes dict.

    return list(shapes_dict.values())               # Return list of shapes.
