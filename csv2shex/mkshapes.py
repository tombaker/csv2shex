"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field, asdict
from typing import List
import ruamel.yaml as yaml
from .config import CSV_ELEMENTS
from .mkstatements import Statement

elements = yaml.safe_load(CSV_ELEMENTS)
SHAPE_ELEMENTS = elements['shape_elements']
STATEMENT_ELEMENTS = elements['statement_elements']


def pprint_shapes(shapes):
    """Pretty-print Shape objects to console."""
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
            pprint_output.append("        Statement\n")
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


@dataclass
class Shape:
    """Holds state and self-validation methods for a Shape."""

    start: bool = False
    shapeID: str = None
    shapeLabel: str = None
    shape_statements: List[Statement] = field(default_factory=list)


def list_shapes(list_of_statement_objects):
    """Return list of Shape objects from list of Statement objects."""
    # pylint: disable=no-member
    # => "E1101: Instance of 'Field' has no 'append' member" - but it does!
    list_of_shape_names_encountered = list()
    aggregator_of_shape_objects = list()
    shape = Shape()
    shape.start = True
    dict_of_statements_for_given_shape = dict()
    first_statement_encountered = True

    # breakpoint()
    for statement in list_of_statement_objects:
        statement.normalize()
        statement.validate()
        statement = asdict(statement)

        if first_statement_encountered:
            if statement["shapeID"]:
                shape.shapeID = statement["shapeID"]
            else:
                shape.shapeID = "http://example.org/default"
            list_of_shape_names_encountered.append(shape.shapeID)
            first_statement_encountered = False

        # If shapeID=None, assign previous shapeID.
        if not statement["shapeID"]:
            shape.shapeID = list_of_shape_names_encountered[-1]

        if statement["shapeID"] not in list_of_shape_names_encountered:
            list_of_shape_names_encountered.append(statement["shapeID"])
            shape = Shape()
            dict_of_statements_for_given_shape = dict()
            shape.shapeID = statement["shapeID"]
            shape.shapeLabel = statement["shapeLabel"]

        # Populate dict_of_statements_for_given_shape by iterating thru keys.
        for pvpair_key in STATEMENT_ELEMENTS:
            dict_of_statements_for_given_shape[pvpair_key] = statement[pvpair_key]

        # breakpoint() 
        # Append dict_of_statements to current shape, add that shape to aggregator.
        shape.shape_statements.append(dict_of_statements_for_given_shape)
        aggregator_of_shape_objects.append(shape)

    pprint_output = pprint_shapes(aggregator_of_shape_objects)
    for line in pprint_output.splitlines():
        print(line)

    return aggregator_of_shape_objects
