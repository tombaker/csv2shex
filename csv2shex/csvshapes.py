"""Class for Python objects derived from CSV files."""


from collections import defaultdict
from dataclasses import dataclass, field, asdict
from typing import List
from .config import SHAPE_ELEMENTS, STATEMENT_ELEMENTS, URI_ELEMENTS
from .csvrows import CSVRow


@dataclass
class CSVShape:
    """Holds state and self-validation methods for a CSVShape."""

    shapeID: str = None
    shapeLabel: str = None
    start: bool = False
    shapeClosed: bool = False
    statement_csvrows_list: List[CSVRow] = field(default_factory=list)


def list_csvshapeobjs(csvrows_list, uri_elements=URI_ELEMENTS, expand_prefixes=False):
    """Return list of CSVShapes from list of CSVRows."""

    csvshapes_ddict = defaultdict(dict)
    is_first_csvrow_encountered = True
    single_statement_dict = dict()

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

        for key in STATEMENT_ELEMENTS:
            single_statement_dict[key] = asdict(csvrow)[key]

        csvshapes_ddict[csvshape.shapeID].statement_csvrows_list.append(
            single_statement_dict.copy()
        )
        single_statement_dict.clear()

    csvshapes_list = []
    for key in csvshapes_ddict.keys():
        csvshapes_list.append(csvshapes_ddict[key])

    # @@@ HERE
    # pylint: disable=unnecessary-pass
    # pylint: disable=unused-variable
    # breakpoint(context=5) 
    if expand_prefixes:
        for shape in csvshapes_list:
            print(shape)
        for element in uri_elements:
            print(element)

    return csvshapes_list


def pprint_schema(csvshape_objs_list, verbose=False):
    """Pretty-print CSVShape objects to console."""
    pprint_output = []
    pprint_output.append("DCAP")
    for csvshape_obj in csvshape_objs_list:
        shap_dict = asdict(csvshape_obj)
        pprint_output.append("    Shape")
        for key in SHAPE_ELEMENTS:
            if not verbose and shap_dict[key]:
                pprint_output.append(8 * " " + key + ": " + str(shap_dict[key]))
            if verbose:
                pprint_output.append(8 * " " + key + ": " + str(shap_dict[key]))

        # breakpoint(context=5)
        for stat_dict in shap_dict["statement_csvrows_list"]:
            pprint_output.append("        Statement")
            for key in STATEMENT_ELEMENTS:
                if not verbose and stat_dict[key]:
                    pprint_output.append(
                        12 * " " + str(key) + ": " + str(stat_dict[key])
                    )
                if verbose:
                    pprint_output.append(
                        12 * " " + str(key) + ": " + str(stat_dict[key])
                    )

    return pprint_output
