"""Class for Python objects derived from CSV files."""


from collections import defaultdict
from dataclasses import dataclass, field, asdict
from typing import List
import ruamel.yaml as yaml
from .config import get_config_settings_dict
from .csvrows import CSVRow
from .expand import _expand_prefixes
from .model import CSV_MODEL


@dataclass
class CSVShape:
    """Holds state and self-validation methods for a CSVShape."""

    shapeID: str = None
    shapeLabel: str = None
    start: bool = False
    shapeClosed: bool = False
    statement_csvrows_list: List[CSVRow] = field(default_factory=list)


def get_csvshapes_dict(
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


def pprint_schema(csvshape_dicts_list, csv_model=CSV_MODEL, verbose=False):
    """Pretty-print CSVShape objects to console."""
    csv_model_dict = yaml.safe_load(csv_model)
    shape_elements = csv_model_dict["shape_elements"]
    statement_elements = csv_model_dict["statement_elements"]

    pprint_output = []
    pprint_output.append("DCAP")
    for csvshape_dict in csvshape_dicts_list:
        pprint_output.append("    Shape")
        for key in shape_elements:
            if not verbose and csvshape_dict[key]:
                pprint_output.append(8 * " " + key + ": " + str(csvshape_dict[key]))
            if verbose:
                pprint_output.append(8 * " " + key + ": " + str(csvshape_dict[key]))

        for stat_dict in csvshape_dict["statement_csvrows_list"]:
            pprint_output.append("        Statement")
            for key in statement_elements:
                if not verbose and stat_dict[key]:
                    pprint_output.append(
                        12 * " " + str(key) + ": " + str(stat_dict[key])
                    )
                if verbose:
                    pprint_output.append(
                        12 * " " + str(key) + ": " + str(stat_dict[key])
                    )

    return pprint_output
