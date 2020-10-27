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
    shapes_list = list()
    shap = Shape()
    shap.start = True
    dict_of_shape_statements = dict()
    # breakpoint()
    # For each statement in aggregated list of statements (from all shapes).
    for statement in list_of_statement_objects:
        statement.normalize()
        statement.validate()
        statement = asdict(statement)
        if shap.shapeID != statement["shapeID"]:
            # if shap.shapeID is not None
            if shap.shapeID:
                shapes_list.append(shap)
            shap = Shape()
            shap.start = statement["start"]
            shap.shapeID = statement["shapeID"]
            shap.shapeLabel = statement["shapeLabel"]

        for pvpair_key in STATEMENT_ELEMENTS:
            dict_of_shape_statements[pvpair_key] = statement[pvpair_key]

        # pylint: disable=no-member
        # => "E1101: Instance of 'Field' has no 'append' member" - but it does!
        shap.shape_statements.append(dict_of_shape_statements)
        dict_of_shape_statements = dict()
    shapes_list.append(shap)
    return shapes_list
