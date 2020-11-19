"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field, asdict
from collections import defaultdict
from typing import List
import ruamel.yaml as yaml
from .config import CSV_MODEL
from .csvrow import CSVRow

CSV_MODEL_DICT = yaml.safe_load(CSV_MODEL)


@dataclass
class CSVShape:
    """Holds state and self-validation methods for a CSVShape."""

    shapeID: str = None
    shapeLabel: str = None
    shapeClosed: str = None
    start: bool = False
    pvdicts_list: List[CSVRow] = field(default_factory=list)


def get_csvshape_dicts_list(csvrow_objs_list, csv_model=CSV_MODEL) -> List[dict]:
    """Get list of csvshape dicts from list of CSVRows."""

    aggregator_ddict = defaultdict(dict)
    is_first_csvrow_encountered = True
    pvdict = dict()
    csv_model_dict = yaml.safe_load(csv_model)

    for csvrow_obj in csvrow_objs_list:
        csvrow_dict = asdict(csvrow_obj)
        if csvrow_dict["shapeID"] not in aggregator_ddict.keys():
            shap_dict = CSVShape()
            shap_dict.shapeID = csvrow_dict["shapeID"]
            shap_dict.shapeLabel = csvrow_dict["shapeLabel"]
            shap_dict.start = bool(is_first_csvrow_encountered)
            shap_dict.pvdicts_list = list()
            aggregator_ddict[shap_dict.shapeID] = shap_dict
            is_first_csvrow_encountered = False

        for key in csv_model_dict["statement_elements"]:
            pvdict[key] = csvrow_dict[key]

        aggregator_ddict[shap_dict.shapeID].pvdicts_list.append(pvdict.copy())
        pvdict.clear()

    # breakpoint(context=5)
    csvshape_dicts_list = []
    for key in aggregator_ddict.keys():
        csvshape_dicts_list.append(asdict(aggregator_ddict[key]))

    return csvshape_dicts_list
