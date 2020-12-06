"""@@@"""

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
import pyjsg
from csv2shex.csvshape import CSVShape, CSVTripleConstraint
from csv2shex.mkshex import get_node_constraint, mkshex


def test_mkshex_mkshex_one_shape():
    """@@@"""
    input_csvshape = CSVShape(
        start=True,
        shapeID=":a",
        tc_list=[
            CSVTripleConstraint(propertyID="dct:creator", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="dct:subject", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="dct:date", valueNodeType="Literal"),
        ],
    )
    schema = mkshex(input_csvshape)
    print(schema)
    assert schema.type == "Schema"
