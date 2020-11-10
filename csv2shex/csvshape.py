"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field, asdict
from collections import defaultdict
from typing import List
import ruamel.yaml as yaml
from .config import CSV_MODEL
from .csvrow import CSVRow
from .expand import _expand_prefixes

CSV_MODEL_DICT = yaml.safe_load(CSV_MODEL)


@dataclass
class CSVShape:
    """Holds state and self-validation methods for a CSVShape."""

    shapeID: str = None
    shapeLabel: str = None
    shapeClosed: str = None
    start: bool = False
    statement_csvrows_list: List[CSVRow] = field(default_factory=list)


def get_csvshape_dicts_list(
    csvrow_objs_list, csv_model=CSV_MODEL, expand_prefixes=False
) -> List[dict]:
    """Get list of CSVShapes (as dicts) from list of CSVRows."""

    csvshapes_ddict = defaultdict(dict)
    is_first_csvrow_encountered = True
    single_statement_dict = dict()
    csv_model_dict = yaml.safe_load(csv_model)
    # prefixes_dict = yaml.safe_load(**CONFIG_SETTINGS)["prefixes"]

    for csvrow in csvrow_objs_list:
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
