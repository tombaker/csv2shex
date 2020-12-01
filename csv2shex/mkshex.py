from typing import Union, List, Optional

from ShExJSG import Schema
from ShExJSG.ShExJ import (
    Shape,
    IRIREF,
    TripleConstraint,
    NodeConstraint,
    shapeExpr,
    OneOf,
)

from csv2shex.csvshape import CSVShape, CSVTripleConstraint


def get_node_constraint(csv_tc: CSVTripleConstraint) -> Optional[shapeExpr]:
    """Generate ShEx node constraint from CSV triple constraint if necessary."""

    rval = None

    def get_nc() -> NodeConstraint:
        return rval if rval else NodeConstraint()

    if csv_tc.valueNodeType:
        #  pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')
        get_nc().nodeKind = csv_tc.valueNodeType.lower()
    if csv_tc.valueConstraint:
        get_nc().values = [csv_tc.valueConstraint]
    if csv_tc.valueConstraintType:
        get_nc().datatype = IRIREF(csv_tc.valueConstraintType)
    if csv_tc.valueShape:
        if rval:
            raise ValueError(
                "Triple constraint cannot have both "
                "a NodeConstraint and a ValueConstraint"
            )
        return IRIREF(csv_tc.valueShape)
    return rval


def addstatement(shape: Shape, statement: CSVStatement) -> None:
    """ Interpret a CSV statement and add shapeExprit to shape """

    # pylint: disable=invalid-name
    # One- and two-letter variable names do not conform to snake-case naming style

    # typing.List[typing.Union["EachOf", "OneOf", "TripleConstraint", typing.Union[str, str]]]
    ts = TripleConstraint(
        id=statement.prop_label,
        predicate=IRIREF(statement.prop_id),
        min=1 if statement.mand else 0,
        max=-1 if statement.repeat else 1,
        valueExpr=statementtonodeconstraint(statement),
    )
    if shape.expression:
        if isinstance(shape.expression, TripleConstraint):
            shape.expression = OneOf(expressions=[shape.expression, ts])
        else:
            shape.expression.expressions.append(ts)
    else:
        shape.expression = ts


def shapetoshex(shapes: Union[CSVShape, List[CSVShape]]) -> Schema:
    """ Convert a list of csv2shape Shapes to a ShEx Schema """

    # pylint: disable=invalid-name
    # One- and two-letter variable names do not conform to snake-case naming style

    if isinstance(shapes, CSVShape):
        shapes = [shapes]
    schema = Schema()
    for s in shapes:
        shape_id = IRIREF(s.shape_id)
        if s.start:
            if schema.start:
                print(f"Multiple start shapes: <{schema.start}>, <{shape_id}>")
            else:
                schema.start = shape_id
        shape = Shape(id=shape_id)
        for statement in s.shape_statements:
            addstatement(shape, statement)
    return schema
