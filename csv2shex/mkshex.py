"""@@@"""

from typing import Union, List, Optional
import pytest
from ShExJSG import Schema
from ShExJSG.ShExJ import (
    Shape,
    IRIREF,
    TripleConstraint,
    NodeConstraint,
    shapeExpr,
    EachOf,
)
# from .csvshape import CSVShape
from .csvrow import CSVRow


def generate_node_constraint(statement: CSVRow) -> Optional[shapeExpr]:
    """Generate a node constraint from statement if necessary."""
    rval = None

    def get_nc() -> NodeConstraint:
        return rval if rval else NodeConstraint()

    if statement.valueNodeType:
        # Note: pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')
        get_nc().nodeKind = statement.valueNodeType.lower()
    if statement.valueConstraint:
        get_nc().values = [statement.valueConstraint]
    if statement.valueConstraintType:
        get_nc().datatype = IRIREF(statement.valueConstraintType)
    if statement.valueShape:
        if rval:
            raise ValueError(
                "CSVRow cannot have both NodeConstraint and ValueConstraint"
            )
        return IRIREF(statement.valueShape)
    return rval


def add_statement(shape: CSVShape, statement: CSVRow) -> None:
    """Interpret a CSV statement and add shapeExpr to shape."""
    # typing.List[typing.Union["EachOf",
    #                          "OneOf",
    #                          "TripleConstraint",
    #                          typing.Union[str, str]]]
    ts = TripleConstraint(
        predicate=IRIREF(statement.propertyID),
        min=1 if statement.mandatory else 0,
        max=-1 if statement.repeatable else 1,
        valueExpr=generate_node_constraint(statement),
    )
    if shape.expression:
        if isinstance(shape.expression, TripleConstraint):
            shape.expression = EachOf(expressions=[shape.expression, ts])
        else:
            shape.expression.expressions.append(ts)
    else:
        shape.expression = ts


def shape_to_shex(shapes: Union[CSVShape, List[CSVShape]]) -> Schema:
    """Convert a list of CSVShapes to a ShEx Schema."""
    if isinstance(shapes, CSVShape):
        shapes = [shapes]
    schema = Schema()
    for s in shapes:
        shapeID = IRIREF(s.shapeID)
        if s.start:
            if schema.start:
                print(f"Multiple start shapes: <{schema.start}>, <{shapeID}>")
            else:
                schema.start = shapeID
        shape = Shape(id=shapeID)
        for statement in s.pvdicts_list:
            add_statement(shape, statement)
    return schema
