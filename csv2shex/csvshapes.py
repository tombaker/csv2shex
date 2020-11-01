"""Class for Python objects derived from CSV files."""


from collections import defaultdict
from dataclasses import dataclass, field, asdict
from typing import List
import ruamel.yaml as yaml
from .config import CSV_ELEMENTS
from .csvrows import CSVRow

elements = yaml.safe_load(CSV_ELEMENTS)
SHAPE_ELEMENTS = elements['shape_elements']
STATEMENT_ELEMENTS = elements['statement_elements']


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

    breakpoint(context=5) 
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

        csvshapes_ddict[csvshape.shapeID].statement_csvrows_list.append(single_statement_dict)
        single_statement_dict.clear()

    csvshapes_list = []
    for key in csvshapes_ddict.keys():
        csvshapes_list.append(csvshapes_ddict[key])

    return csvshapes_list


def pprint_shapes(shapes):
    """Pretty-print CSVShape objects to console."""
    pprint_output = []
    pprint_output.append("DCAP\n")
    for shape in shapes:
        shape = asdict(shape)
        pprint_output.append("    Shape\n")
        for shape_key in SHAPE_ELEMENTS:
            if shape[shape_key]:
                pprint_output.append(
                    "        " + str(shape_key) + ": " + str(shape[shape_key]) + "\n"
                )
        for statement in shape["statement_csvrows_list"]:
            pprint_output.append("        CSVRow\n")
            for statement_key in STATEMENT_ELEMENTS:
                if statement[statement_key]:
                    pprint_output.append(
                        "            "
                        + str(statement_key)
                        + ": "
                        + str(statement[statement_key])
                        + "\n"
                    )
    return "".join(pprint_output)
