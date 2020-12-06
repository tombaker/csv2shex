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
from jsonasobj import as_json, loads
from pyshex.utils.schema_loader import SchemaLoader
from pyshexc.ShExC import ShExC
from csv2shex.csvshape import CSVShape, CSVTripleConstraint
from csv2shex.mkshex import get_node_constraint, mkshex, mkshexj

EXPECTED = """
{
   "type": "Schema",
   "@context": "http://www.w3.org/ns/shex.jsonld",
   "start": ":a",
   "shapes": [
      {
         "type": "Shape",
         "id": ":a",
         "expression": {
            "type": "EachOf",
            "expressions": [
               {
                  "type": "TripleConstraint",
                  "predicate": "http://purl.org/dc/terms/creator",
                  "valueExpr": {
                     "type": "NodeConstraint",
                     "nodeKind": "iri"
                  },
                  "min": 0,
                  "max": 1
               },
               {
                  "type": "TripleConstraint",
                  "predicate": "http://purl.org/dc/terms/subject",
                  "valueExpr": {
                     "type": "NodeConstraint",
                     "nodeKind": "iri"
                  },
                  "min": 0,
                  "max": 1
               },
               {
                  "type": "TripleConstraint",
                  "predicate": "http://purl.org/dc/terms/date",
                  "valueExpr": {
                     "type": "NodeConstraint",
                     "nodeKind": "literal"
                  },
                  "min": 0,
                  "max": 1
               }
            ]
         }
      }
   ]
}"""

EXPECTED_SHEXC = """
n START= @:a
:a { ( dct:creator IRI ? ; <dct:subject>
 IRI ? ; dct:date LITERAL ? ) }
"""


def test_mkshex_mkshex_one_shape():
    """@@@"""
    input_csvshape = CSVShape(
        start=True,
        shapeID=":a",
        tc_list=[
            CSVTripleConstraint(propertyID="http://purl.org/dc/terms/creator", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="http://purl.org/dc/terms/subject", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="http://purl.org/dc/terms/date", valueNodeType="Literal"),
        ],
    )
    schema = mkshex(input_csvshape)
    print("\nn" + str(ShExC(mkshex(input_csvshape))))
    assert mkshex(input_csvshape) == SchemaLoader().loads(EXPECTED)
    assert mkshexj(input_csvshape) == as_json(mkshex(input_csvshape))
