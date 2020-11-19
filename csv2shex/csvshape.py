"""Class for Python objects derived from CSV files."""


from collections import defaultdict
from typing import List
import ruamel.yaml as yaml
from .config import CSV_MODEL

CSV_MODEL_DICT = yaml.safe_load(CSV_MODEL)


def get_csvshape_dicts_list(csvrow_dicts_list, csv_model=CSV_MODEL) -> List[dict]:
    """Get list of csvshape dicts from list of csvrow dicts."""

    aggregator_ddict = defaultdict(dict)
    is_first_csvrow_encountered = True
    pvdict = dict()
    csv_model_dict = yaml.safe_load(csv_model)

    for csvrow_dict in csvrow_dicts_list:
        if csvrow_dict["shapeID"] not in aggregator_ddict.keys():
            shap_dict = dict()
            shap_dict["shapeID"] = csvrow_dict["shapeID"]
            shap_dict["shapeLabel"] = csvrow_dict["shapeLabel"]
            shap_dict["shapeClosed"] = csvrow_dict["shapeClosed"]
            shap_dict["start"] = bool(is_first_csvrow_encountered)
            shap_dict["pvdicts_list"] = list()
            aggregator_ddict[shap_dict["shapeID"]] = shap_dict
            is_first_csvrow_encountered = False

        for key in csv_model_dict["cvpair_elements"]:
            pvdict[key] = csvrow_dict[key]

        aggregator_ddict[shap_dict["shapeID"]]["pvdicts_list"].append(pvdict.copy())
        pvdict.clear()

    csvshape_dicts_list = []
    for key in aggregator_ddict.keys():
        csvshape_dict = aggregator_ddict[key]
        csvshape_dicts_list.append(csvshape_dict)

    return csvshape_dicts_list
