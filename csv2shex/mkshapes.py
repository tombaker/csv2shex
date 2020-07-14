"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field, asdict
from typing import List
from .constants import STATEMENT_KEYS, SHAPE_KEYS
from .mkstatements import Statement


def pprint_shapes(shapes):
    """Pretty-print Shape objects to console."""
    pprint_output = []
    for shape in shapes:
        shape = asdict(shape)
        pprint_output.append("Shape\n")
        for shape_key in SHAPE_KEYS:
            if shape[shape_key]:
                pprint_output.append(
                    "    " + str(shape_key) + ": " + str(shape[shape_key]) + "\n"
                )
        for statement in shape["shape_statements"]:
            pprint_output.append("    Statement\n")
            for statement_key in STATEMENT_KEYS:
                if statement[statement_key]:
                    pprint_output.append(
                        "        "
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
    shape_id: str = None
    shape_label: str = None
    shape_statements: List(Statement) = field(default_factory=list)


def list_shapes(statements_list):
    """Return list of Shape objects from list of Statement objects."""
    shapes_list = list()
    shap = Shape()
    shape_statements_item = dict()
    for statement in statements_list:
        statement = asdict(statement)
        if shap.shape_id != statement["shape_id"]:
            # if shap.shape_id is not None
            if shap.shape_id:
                shapes_list.append(shap)
            shap = Shape()
            shap.start = statement["start"]
            shap.shape_id = statement["shape_id"]
            shap.shape_label = statement["shape_label"]

        for pvpair_key in STATEMENT_KEYS:
            shape_statements_item[pvpair_key] = statement[pvpair_key]

        # pylint: disable=no-member
        # => "E1101: Instance of 'Field' has no 'append' member" - but it does!
        shap.shape_statements.append(shape_statements_item)
        shape_statements_item = dict()
    shapes_list.append(shap)
    return shapes_list
