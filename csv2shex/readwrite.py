"""Read DCAP/CSV. Write and read config file."""

import os
import csv
from pathlib import Path
import ruamel.yaml as yaml
from .csvrows import CSVRow
from .settings import (
    DEFAULT_CONFIGFILE_NAME,
    DEFAULT_CONFIG_SETTINGS_YAML,
    CSV_MODEL,
    write_starter_configfile,
    get_config_settings_dict,
)
from .exceptions import CsvError, ConfigError

CSV_MODEL_DICT = yaml.safe_load(CSV_MODEL)


def csvreader(csvfile):
    """Read CSV file and return list of dicts, one dict per CSV row."""
    csv_dictreader_obj = csv.DictReader(
        Path(csvfile).open(newline="", encoding="utf-8-sig")
    )
    csvrow_dicts_list = list(csv_dictreader_obj)
    if "propertyID" not in list(csvrow_dicts_list[0].keys()):
        raise CsvError("To be valid, DCAP CSV must have a 'propertyID' column header.")
    return csvrow_dicts_list


def get_csvrowobjs_list(csvrow_dicts_list=None, csv_model_dict=CSV_MODEL_DICT):
    """Turn list of dicts into list of CSVRow objects."""
    csvrows_list = []
    shapeids_list = []
    first_shape_encountered = True
    shape_elements = csv_model_dict["shape_elements"]
    statement_elements = csv_model_dict["statement_elements"]
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

        csvrows_list.append(stat)
    return csvrows_list
