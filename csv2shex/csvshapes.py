"""Class for Python objects derived from CSV files."""


from collections import defaultdict
from dataclasses import dataclass, field, asdict
from typing import List
import ruamel.yaml as yaml
from .config import CSV_ELEMENTS
from .csvrows import CSVRow

elements = yaml.safe_load(CSV_ELEMENTS)
SHAPE_ELEMENTS = elements["shape_elements"]
STATEMENT_ELEMENTS = elements["statement_elements"]


@dataclass
class CSVShape:
    """Holds state and self-validation methods for a CSVShape."""

    shapeID: str = None
    shapeLabel: str = None
    start: bool = False
    shapeClosed: bool = False
    statement_csvrows_list: List[CSVRow] = field(default_factory=list)


def list_csvshapes(csvrows_list):
    """Return list of CSVShapes from list of CSVRows."""

    # shapeLabel-to-csvshape_dict
    csvshapes_ddict = defaultdict(dict)
    is_first_csvrow_encountered = True
    single_statement_dict = dict()

    # breakpoint(context=5)
    for csvrow in csvrows_list:
        csvrow.normalize()
        csvrow.validate()
        if csvrow.shapeID not in csvshapes_ddict.keys():
            csvshape = CSVShape()
            csvshape.shapeID = csvrow.shapeID
            csvshape.shapeLabel = csvrow.shapeLabel
            csvshape.start = True if is_first_csvrow_encountered else False
            csvshapes_ddict[csvshape.shapeID] = csvshape
            is_first_csvrow_encountered = False

        for key in STATEMENT_ELEMENTS:
            single_statement_dict[key] = asdict(csvrow)[key]

        csvshapes_ddict[csvshape.shapeID].statement_csvrows_list.append(
            single_statement_dict.copy()
        )
        single_statement_dict.clear()

    csvshapes_list = []
    for key in csvshapes_ddict.keys():
        csvshapes_list.append(csvshapes_ddict[key])

    return csvshapes_list


def pprint_shapes(csvshape_objs_list, verbose=False):
    """Pretty-print CSVShape objects to console."""
    pprint_output = []
    pprint_output.append("DCAP")
    for csvshape_obj in csvshape_objs_list:
        shap_dict = asdict(csvshape_obj)
        pprint_output.append("    Shape")
        for key in SHAPE_ELEMENTS:
            if shap_dict[key] and not verbose:
                pprint_output.append(8*" " + key + ": " + str(shap_dict[key]))
            if verbose:
                pprint_output.append(8*" " + key + ": " + str(shap_dict[key]))
        
        # breakpoint(context=5)
        for stat_dict in shap_dict["statement_csvrows_list"]:
            pprint_output.append("        Statement")
            for key in STATEMENT_ELEMENTS:
                if stat_dict[key] and not verbose:
                    pprint_output.append(12*" " + str(key) + ": " + str(stat_dict[key]))
                if verbose:
                    pprint_output.append(12*" " + str(key) + ": " + str(stat_dict[key]))

    return pprint_output
