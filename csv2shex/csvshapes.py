"""Class for Python objects derived from CSV files."""


from collections import defaultdict
from dataclasses import dataclass, field, asdict
from typing import List
import ruamel.yaml as yaml
from .model import CSV_ELEMENTS
from .csvrows import CSVRow


@dataclass
class CSVShape:
    """Holds state and self-validation methods for a CSVShape."""

    shapeID: str = None
    shapeLabel: str = None
    start: bool = False
    shapeClosed: bool = False
    statement_csvrows_list: List[CSVRow] = field(default_factory=list)


def get_csvshapes_dict(
    csvrows_list, csv_elements=CSV_ELEMENTS, expand_prefixes=False
) -> List[dict]:
    """Get list of CSVShapes (as dicts) from list of CSVRows."""

    csvshapes_ddict = defaultdict(dict)
    is_first_csvrow_encountered = True
    single_statement_dict = dict()

    csv_elements_dict = yaml.safe_load(csv_elements)
    shape_uri_elements = csv_elements_dict["shape_uri_elements"]
    statement_uri_elements = csv_elements_dict["statement_uri_elements"]

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

        for key in statement_uri_elements:
            single_statement_dict[key] = asdict(csvrow)[key]

        csvshapes_ddict[csvshape.shapeID].statement_csvrows_list.append(
            single_statement_dict.copy()
        )
        single_statement_dict.clear()

    csvshape_dicts_list = []
    for key in csvshapes_ddict.keys():
        csvshape_dicts_list.append(asdict(csvshapes_ddict[key]))

    # @@@ HERE
    # pylint: disable=unnecessary-pass
    # pylint: disable=unused-variable
    # breakpoint(context=5)
    if expand_prefixes:
        for shape in csvshape_dicts_list:
            for element in shape_uri_elements:
                print(shape[element])
                shape[element] = ":bar"
                print(shape[element])
            for element in statement_uri_elements:
                pass
                # for csvrow in element['statement_csvrows_list']:

    return csvshape_dicts_list


def pprint_schema(csvshape_dicts_list, csv_elements=CSV_ELEMENTS, verbose=False):
    """Pretty-print CSVShape objects to console."""
    csv_elements_dict = yaml.safe_load(csv_elements)
    shape_elements = csv_elements_dict["shape_elements"]
    statement_elements = csv_elements_dict["statement_elements"]

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
