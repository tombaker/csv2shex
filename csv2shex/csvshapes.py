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
    shape_statements: List[CSVRow] = field(default_factory=list)


def list_csvshapes(list_of_statement_objects):
    """Return list of CSVShape objects from list of CSVRow objects."""
    # pylint: disable=no-member
    # => "E1101: Instance of 'Field' has no 'append' member" - but it does!
    list_of_shape_names_encountered = list()

    from collections import defaultdict
    aggregator_of_shape_objects = defaultdict(dict)
    first_statement_encountered = True

    breakpoint()
    for statement in list_of_statement_objects:
        statement.normalize()
        statement.validate()
        statement = asdict(statement)

        # Initializes new shapes as encountered
        if statement["shapeID"] not in list_of_shape_names_encountered:
            shape = CSVShape()
            shape.shapeID = statement["shapeID"]
            shape.shapeLabel = statement["shapeLabel"]
            list_of_shape_names_encountered.append(statement["shapeID"])
            dict_of_statements_for_given_shape = dict()

        if first_statement_encountered:
            shape.start = True
            first_statement_encountered = False

        # Add key-value pairs of statement to dict_of_statements_for_given_shape.
        for pvpair_key in STATEMENT_ELEMENTS:
            dict_of_statements_for_given_shape[pvpair_key] = statement[pvpair_key]

        # Append dict_of_statements to current shape, add that shape to aggregator.
        shape.shape_statements.append(dict_of_statements_for_given_shape)
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
        for statement in shape["shape_statements"]:
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
