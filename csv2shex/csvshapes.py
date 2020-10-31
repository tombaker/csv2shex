"""Class for Python objects derived from CSV files."""


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
    shape_csvrows: List[CSVRow] = field(default_factory=list)


def list_csvshapes(csvrows_list):
    """Return list of CSVShape objects from list of CSVRow objects."""
    # pylint: disable=no-member
    # => "E1101: Instance of 'Field' has no 'append' member" - but it does!
    csvshape_ids_list = list()

    from collections import defaultdict
    dict_for_csvshape_objs = defaultdict(dict)
    first_csvrow_encountered = True

    # breakpoint()
    for csvrow in csvrows_list:
        csvrow.normalize()
        csvrow.validate()
        csvrow = asdict(csvrow)

        # Initializes new csvshapes as encountered
        if csvrow["shapeID"] not in csvshape_ids_list:
            csvshape = CSVShape()
            csvshape.shapeID = csvrow["shapeID"]
            csvshape.shapeLabel = csvrow["shapeLabel"]
            csvshape_ids_list.append(csvrow["shapeID"])
            csvshapeid_to_csvrows_dict = dict()

        if first_csvrow_encountered:
            csvshape.start = True
            first_csvrow_encountered = False

        # Add key-value pairs of csvrow to csvshapeid_to_csvrows_dict.
        for pvpair_key in STATEMENT_ELEMENTS:
            csvshapeid_to_csvrows_dict[pvpair_key] = csvrow[pvpair_key]

        # Append dict of CSVRows to current shape, add that shape to aggregator.
        csvshape.shape_csvrows.append(csvshapeid_to_csvrows_dict)
        dict_for_csvshape_objs[csvshape.shapeID] = csvshape

    #pprint_output = pprint_shapes(dict_for_csvshape_objs)
    #for line in pprint_output.splitlines():
    #    print(line)

    return [ dict_for_csvshape_objs[key] for key in dict_for_csvshape_objs.keys() ]


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
        for statement in shape["shape_csvrows"]:
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
