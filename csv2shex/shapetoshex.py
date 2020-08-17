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

from csv2shex.mkshapes import Shape as CSVShape, Statement as CSVStatement


# Questions:
# 1) is s.shape_id always present or do we have to supply it?
#    A: According to mkstatements, will always be present.
# 2) What is the shape label used for?
#    A: probably nothing except documentation.  Should we embed it as a comment?
# 3) Are multiple shape statements considered ShapeOr or ShapeAnd?
#    We are assuming AND for the time being
# 4) We assign prop_label to statement.id, but but there may be labels
#    that don't fit the id value space
# 5) Need to define how "prefixed URI string" maps to IRIREF
#    -- probably need a sub function


def statementtonodeconstraint(statement: CSVStatement) -> Optional[shapeExpr]:
    """ Generate a node constraint from statement if necessary """
    rval = None

    def get_nc() -> NodeConstraint:
        return rval if rval else NodeConstraint()

    if statement.value_type:
        #  pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')
        get_nc().nodeKind = statement.value_type.lower()
    if statement.constraint_value:
        get_nc().values = [statement.constraint_value]
    if statement.constraint_type:
        get_nc().datatype = IRIREF(statement.constraint_type)
    if statement.shape_ref:
        if rval:
            raise ValueError(
                "Statement cannot have both NodeConstraint and ValueConstraint"
            )
        return IRIREF(statement.shape_ref)
    return rval


def addstatement(shape: Shape, statement: CSVStatement) -> None:
    """ Interpret a CSV statement and add shapeExprit to shape """
    # typing.List[typing.Union["EachOf",
    #                          "OneOf",
    #                          "TripleConstraint",
    #                          typing.Union[str, str]]]
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
