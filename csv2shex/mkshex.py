"""Convert list of CSVShape instances into ShEx Schema."""

from typing import Union, List, Optional

from rdflib import Namespace
from ShExJSG import Schema
from ShExJSG.ShExJ import (
    Shape,
    IRIREF,
    TripleConstraint,
    NodeConstraint,
    shapeExpr,
    EachOf,
)

from csv2shex.csvshape import CSVShape, CSVTripleConstraint


def get_node_constraint(csv_tc: CSVTripleConstraint) -> Optional[shapeExpr]:
    """Generate ShEx node constraint from CSV triple constraint if necessary."""

    rval = None

    def get_nc() -> NodeConstraint:
        return rval if rval else NodeConstraint()

    nc = get_nc()
    if csv_tc.valueNodeType:
        #  pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')
        nc.nodeKind = csv_tc.valueNodeType.lower()
#    if csv_tc.valueConstraint:
#        get_nc().values = [csv_tc.valueConstraint]
#    if csv_tc.valueConstraintType:
#        get_nc().datatype = IRIREF(csv_tc.valueConstraintType)
#    if csv_tc.valueShape:
#        if rval:
#            raise ValueError(
#                "Triple constraint cannot have both "
#                "a NodeConstraint and a ValueConstraint"
#            )
#        return IRIREF(csv_tc.valueShape)
#    return rval
    return nc


def add_triple_constraint(shape: Shape, csv_tc: CSVTripleConstraint) -> None:
    """Interpret CSV triple constraint and add shapeExpr to shape."""

    # pylint: disable=invalid-name
    # two-letter variable names do not conform to snake-case naming style

    # typing.List[typing.Union["EachOf", "OneOf", "TripleConstraint", typing.Union[str, str]]]
    ts = TripleConstraint(
        # Why does a triple constraint need to have a label?
        # id=csv_tc.prop_label,
        predicate=IRIREF(csv_tc.propertyID),
        min=1 if csv_tc.mandatory else 0,
        max=-1 if csv_tc.repeatable else 1,
        valueExpr=get_node_constraint(csv_tc),
    )
    if shape.expression:
        if isinstance(shape.expression, TripleConstraint):
            shape.expression = EachOf(expressions=[shape.expression, ts])
        else:
            shape.expression.expressions.append(ts)
    else:
        shape.expression = ts


def mkshex(shapes: Union[CSVShape, List[CSVShape]]) -> Schema:
    """Convert a list of csv2shape Shapes to a ShEx Schema."""

    # pylint: disable=invalid-name
    # One- and two-letter variable names do not conform to snake-case naming style


    if isinstance(shapes, CSVShape):
        shapes = [shapes]
    schema = Schema()
    for s in shapes:
        shape_id = IRIREF(s.shapeID)
        if s.start:
            if schema.start:
                print(f"Multiple start shapes: <{schema.start}>, <{shape_id}>")
            else:
                schema.start = shape_id
        shape = Shape(id=shape_id)
        for csv_tc in s.tc_list:
            add_triple_constraint(shape, csv_tc)
        if not schema.shapes:
            schema.shapes = [shape]
        else:
            schema.shapes.append(shape)
    return schema
