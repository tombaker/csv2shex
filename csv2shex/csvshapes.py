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


def list_csvshapes(list_of_csvrow_objects):
    """Return list of CSVShape objects from list of CSVRow objects."""
    # pylint: disable=no-member
    # => "E1101: Instance of 'Field' has no 'append' member" - but it does!
    list_of_shape_names_encountered = list()

    from collections import defaultdict
    aggregator_of_shape_objects = defaultdict(dict)
    first_csvrow_encountered = True

    breakpoint()
    for csvrow in list_of_csvrow_objects:
        csvrow.normalize()
        csvrow.validate()
        csvrow = asdict(csvrow)

        # Initializes new shapes as encountered
        if csvrow["shapeID"] not in list_of_shape_names_encountered:
            shape = CSVShape()
            shape.shapeID = csvrow["shapeID"]
            shape.shapeLabel = csvrow["shapeLabel"]
            list_of_shape_names_encountered.append(csvrow["shapeID"])
            dict_of_statements_for_given_shape = dict()

        if first_csvrow_encountered:
            shape.start = True
            first_csvrow_encountered = False

        # Add key-value pairs of csvrow to dict_of_statements_for_given_shape.
        for pvpair_key in STATEMENT_ELEMENTS:
            dict_of_statements_for_given_shape[pvpair_key] = csvrow[pvpair_key]

        # Append dict_of_statements to current shape, add that shape to aggregator.
        shape.shape_csvrows.append(dict_of_statements_for_given_shape)
        aggregator_of_shape_objects.append(shape)

    pprint_output = pprint_shapes(aggregator_of_shape_objects)
    for line in pprint_output.splitlines():
        print(line)

    return aggregator_of_shape_objects


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
