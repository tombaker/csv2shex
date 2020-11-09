"""Read DCAP/CSV (expand prefixes?). Write and read config file."""

import csv
from dataclasses import asdict
from collections import defaultdict
from pathlib import Path
from typing import List
import ruamel.yaml as yaml
from .csvrow import CSVRow
from .csvshape import CSVShape
from .expand import _expand_prefixes
from .settings import CSV_MODEL
from .exceptions import CsvError

CSV_MODEL_DICT = yaml.safe_load(CSV_MODEL)


def csvreader(csvfile):
    """Read CSV file and return list of dicts, one dict per CSV row."""
    csv_dictreader_obj = csv.DictReader(
        Path(csvfile).open(newline="", encoding="utf-8-sig")
    )
    csvrow_dicts_list = list(csv_dictreader_obj)
    if "propertyID" not in list(csvrow_dicts_list[0].keys()):
        raise CsvError("Valid DCAP CSV must have a 'propertyID' column.")
    return csvrow_dicts_list


def get_csvrow_objs_list(csvrow_dicts_list=None, csv_model_dict=CSV_MODEL_DICT):
    """Turn list of dicts into list of CSVRow objects."""
    csvrow_objs_list = []
    shapeids_list = []
    first_shape_encountered = True
    keys = csv_model_dict["shape_elements"] + csv_model_dict["statement_elements"]
    keys.remove("shapeID")
    for row in csvrow_dicts_list:
        if not row.get("propertyID") and row.get("shapeID"):
            shapeids_list.append(row["shapeID"])
            continue

        stat = CSVRow()

        if row.get("shapeID"):
            stat.shapeID = row["shapeID"]
        else:
            if shapeids_list:
                stat.shapeID = shapeids_list[-1]
            elif not shapeids_list:
                stat.shapeID = ":default"
        if stat.shapeID not in shapeids_list:
            shapeids_list.append(stat.shapeID)
        if first_shape_encountered:
            first_shape_encountered = False

        for key in keys:
            if key in row:
                setattr(stat, key, row[key])

        csvrow_objs_list.append(stat)
    return csvrow_objs_list


def get_csvshape_dicts_list(
    csvrows_list, csv_model=CSV_MODEL, expand_prefixes=False
) -> List[dict]:
    """Get list of CSVShapes (as dicts) from list of CSVRows."""

    csvshapes_ddict = defaultdict(dict)
    is_first_csvrow_encountered = True
    single_statement_dict = dict()
    csv_model_dict = yaml.safe_load(csv_model)
    # prefixes_dict = yaml.safe_load(**CONFIG_SETTINGS)["prefixes"]

    for csvrow in csvrows_list:
        csvrow.normalize()
        csvrow.validate()
        if csvrow.shapeID not in csvshapes_ddict.keys():
            csvshape = CSVShape()
            csvshape.shapeID = csvrow.shapeID
            csvshape.shapeLabel = csvrow.shapeLabel
            csvshape.start = bool(is_first_csvrow_encountered)
            csvshapes_ddict[csvshape.shapeID] = csvshape
            is_first_csvrow_encountered = False

        # breakpoint(context=5)
        for key in csv_model_dict["statement_elements"]:
            single_statement_dict[key] = asdict(csvrow)[key]

        csvshapes_ddict[csvshape.shapeID].statement_csvrows_list.append(
            single_statement_dict.copy()
        )
        single_statement_dict.clear()

    csvshape_dicts_list = []
    for key in csvshapes_ddict.keys():
        csvshape_dicts_list.append(asdict(csvshapes_ddict[key]))

    if expand_prefixes:
        _expand_prefixes(csvshape_dicts_list, csv_model_dict=csv_model_dict)
        # also prefixes_dict=prefixes_dict?

    return csvshape_dicts_list
