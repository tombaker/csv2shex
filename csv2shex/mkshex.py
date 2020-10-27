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
#    Normalized CSVStatement objects are always supposed to have 
#    a 'shapeID' object. If 'shapeID' is None, 'shapeID' of previous 
#    statement is assigned.
#    Q: Current default is "default" - is there a conventional name to use?
# 2) What is the shape label used for?
#    A: shapeID is the shape identifier; shapeLabel is a human-readable label,
#    only for documentation.
#    Q: Should we embed it as a comment in ShEx?
#    A: Yes - or optionally generate UI (form-building) statements (eg sh:group)?
#    Let's ignore these annotations for now...
# 3) Are multiple shape statements considered ShapeOr or ShapeAnd?
#    We are assuming AND for the time being.
#    Q: Do not understand ShapeOr...
# 4) We assign propertyLabel to statement.id, but but there may be labels
#    that don't fit the id value space
#    A: propertyID is the identifier; propertyLabel is just a human-readable label
# 5) Need to define how "prefixed URI string" maps to IRIREF
#    -- probably need a sub function
#    A: Maybe use prefix declarations to expand all prefixed URI strings.
#       - as defined in csv2shex.config.PREFIXES (built-in)
#       - as defined (or pointed to) in a csv2shex config file?
#       - as defined in a config file as per a CLI option?


def statement_to_node_constraint(statement: CSVStatement) -> Optional[shapeExpr]:
    """ Generate a node constraint from statement if necessary """
    rval = None

    def get_nc() -> NodeConstraint:
        return rval if rval else NodeConstraint()

    if statement.valueNodeType:
        #  pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')
        get_nc().nodeKind = statement.valueNodeType.lower()
    if statement.valueConstraint:
        get_nc().values = [statement.valueConstraint]
    if statement.valueConstraintType:
        get_nc().datatype = IRIREF(statement.valueConstraintType)
    if statement.valueShape:
        if rval:
            raise ValueError(
                "Statement cannot have both NodeConstraint and ValueConstraint"
            )
        return IRIREF(statement.valueShape)
    return rval


def add_statement(shape: Shape, statement: CSVStatement) -> None:
    """ Interpret a CSV statement and add shapeExprit to shape """
    # typing.List[typing.Union["EachOf",
    #                          "OneOf",
    #                          "TripleConstraint",
    #                          typing.Union[str, str]]]
    ts = TripleConstraint(
        id=statement.propertyLabel,     # what is this?
        predicate=IRIREF(statement.propertyID),
        min=1 if statement.mandatory else 0,
        max=-1 if statement.repeatable else 1,
        valueExpr=statement_to_node_constraint(statement),
    )
    if shape.expression:
        if isinstance(shape.expression, TripleConstraint):
            shape.expression = EachOf(expressions=[shape.expression, ts])
        else:
            shape.expression.expressions.append(ts)
    else:
        shape.expression = ts


def shape_to_shex(shapes: Union[CSVShape, List[CSVShape]]) -> Schema:
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
            add_statement(shape, statement)
    return schema
