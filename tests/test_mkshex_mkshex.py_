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
from csv2shex.mkshex import get_node_constraint, mkshex

expected = """
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

expected_shex = """
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
            CSVTripleConstraint(propertyID="dct:creator", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="dct:subject", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="dct:date", valueNodeType="Literal"),
        ],
    )
    x = mkshex(input_csvshape)
    # print(as_json(mkshex(input_csvshape)))
    print("\nn" + str(ShExC(mkshex(input_csvshape))))
    assert mkshex(input_csvshape) == SchemaLoader().loads(expected)
