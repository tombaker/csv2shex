"""Reader of CSV files."""


import csv
from pathlib import Path
from .exceptions import CsvError


def csvreader(csvfile):
    """Read CSV file and return list of dicts, one dict per CSV row."""
    csv_dictreader_obj = csv.DictReader(Path(csvfile).open(newline="", encoding="utf-8-sig"))
    csvrow_dicts_list = list(csv_dictreader_obj)
    if "propertyID" not in list(csvrow_dicts_list[0].keys()):
        raise CsvError("To be valid, DCAP CSV must have a 'propertyID' column header.")
    return csvrow_dicts_list
