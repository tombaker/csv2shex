"""Reader of CSV files."""


import csv
from pathlib import Path
from .exceptions import CsvError

# from .utils import is_uri, is_valid_uri_or_prefixed_uri

# pylint: disable=no-self-use,too-many-branches,too-many-instance-attributes
# => self-use: for now...
# => too-many-branches: a matter of taste?
# => too-many-instance-attributes: disagree!


def csvreader(csvfile):
    """Read CSV file and return list of dicts, one dict per CSV row."""
    csv_dictreader_obj = csv.DictReader(Path(csvfile).open(newline="", encoding="utf-8-sig"))
    csvrow_dicts_list = list(csv_dictreader_obj)
    if "propertyID" not in list(csvrow_dicts_list[0].keys()):
        raise CsvError("To be valid, DCAP CSV must have a 'propertyID' column header.")
    return csvrow_dicts_list
