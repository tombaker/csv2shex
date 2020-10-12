"""@@@"""

from typing import Union, List, Optional

from ShExJSG import Schema
from ShExJSG.ShExJ import (
    Shape,
    IRIREF,
    TripleConstraint,
    NodeConstraint,
    shapeExpr,
    EachOf,
)

from csv2shex.mkshapes import Shape as CSVShape, Statement as CSVStatement


# Questions:
# 1) is s.shapeID always present or do we have to supply it?
#    A: According to mkstatements, will always be present.
#    Q: Current default is "default" - is there a conventional name to use?
# 2) What is the shape label used for?
#    A: probably nothing except documentation.
#    Q: Should we embed it as a comment in ShEx?
#    A: Yes - or optionally generate UI (form-building) statements (eg sh:group)?
# 3) Are multiple shape statements considered ShapeOr or ShapeAnd?
#    We are assuming AND for the time being
# 4) We assign prop_label to statement.id, but but there may be labels
#    that don't fit the id value space
# 5) Need to define how "prefixed URI string" maps to IRIREF
#    -- probably need a sub function
#    A: Maybe use prefix declarations to expand all prefixed URI strings.
#       - as defined in csv2shex.config.PREFIXES (built-in)
#       - as defined (or pointed to) in a csv2shex config file?
#       - as defined in a config file as per a CLI option?


def statementtonodeconstraint(statement: CSVStatement) -> Optional[shapeExpr]:
    """ Generate a node constraint from statement if necessary """
    rval = None

    def get_nc() -> NodeConstraint:
        return rval if rval else NodeConstraint()

    if statement.value_node_type:
        #  pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')
        get_nc().nodeKind = statement.value_node_type.lower()
    if statement.value_constraint:
        get_nc().values = [statement.value_constraint]
    if statement.value_constraint_type:
        get_nc().datatype = IRIREF(statement.value_constraint_type)
    if statement.value_shape:
        if rval:
            raise ValueError(
                "Statement cannot have both NodeConstraint and ValueConstraint"
            )
        return IRIREF(statement.value_shape)
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
            shape.expression = EachOf(expressions=[shape.expression, ts])
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
        shapeID = IRIREF(s.shapeID)
        if s.start:
            if schema.start:
                print(f"Multiple start shapes: <{schema.start}>, <{shapeID}>")
            else:
                schema.start = shapeID
        shape = Shape(id=shapeID)
        for statement in s.shape_statements:
            addstatement(shape, statement)
    return schema
