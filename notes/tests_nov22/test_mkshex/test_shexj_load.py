import os
import pytest
from typing import cast

from ShExJSG import ShExC, ShExJ
from ShExJSG.SchemaWithContext import Schema
from ShExJSG.ShExJ import Shape, EachOf, TripleConstraint, NodeConstraint, IriStem
from pyjsg.jsglib import loader
from pyjsg.jsglib.loader import is_valid, StringIO
from pyshex.utils.schema_loader import SchemaLoader
from rdflib import DCTERMS

from tests import EXAMPLE_PROFILES_DIRECTORY

from pyjsg.jsglib.jsg_array import JSGArray


def test_shexj_from_text():
    """ Load ShEx JSON text string """
    shex_json = """
    {
       "@context": "http://www.w3.org/ns/shex.jsonld",
       "type": "Schema",
       "shapes": [
          {
              "type": "Shape",
              "id": "http://example.org/myshape",
              "expression": {
                 "type": "EachOf",
                 "expressions": [
                   {
                     "type": "TripleConstraint",
                     "predicate": "http://purl.org/dc/terms/title",
                     "valueExpr": {
                       "type": "NodeConstraint",
                       "nodeKind": "literal"
                     },
                     "min": "1",
                     "max": "-1"
                   },
                   {
                     "type": "TripleConstraint",
                     "predicate": "http://purl.org/dc/terms/description",
                     "valueExpr": {
                       "type": "NodeConstraint",
                       "datatype": "http://www.w3.org/2001/XMLSchema#string"
                     }
                   },
                   {
                     "type": "TripleConstraint",
                     "predicate": "http://purl.org/dc/terms/subject",
                     "valueExpr": {
                       "type": "NodeConstraint",
                       "values": [
                          {
                             "type": "IriStem",
                             "stem": "http://lod.nal.usda.gov/nalt/"
                          }
                       ]
                     }
                   },
                   {
                     "type": "TripleConstraint",
                     "predicate": "http://purl.org/dc/terms/creator",
                     "valueExpr": "http://example.org/mycreator"
                   }
                ]
             }
          }
       ]
    }
    """
    shex = SchemaLoader().loads(shex_json)
    assert isinstance(shex, ShExJ.Schema)
    assert isinstance(shex.shapes[0], Shape)
    assert shex.shapes[0].type == "Shape"
    assert shex.shapes[0].id == "http://example.org/myshape"

    assert shex.shapes[0].expression.type == "EachOf"
    assert isinstance(shex.shapes[0].expression, EachOf)
    assert isinstance(shex.shapes[0].expression.expressions, JSGArray)
    assert isinstance(shex.shapes[0].expression.expressions[0], TripleConstraint)

    assert shex.shapes[0].expression.expressions[0].type == "TripleConstraint"
    assert (
        shex.shapes[0].expression.expressions[0].predicate
        == "http://purl.org/dc/terms/title"
    )
    assert shex.shapes[0].expression.expressions[0].min == 1
    assert shex.shapes[0].expression.expressions[0].max == -1
    assert isinstance(
        shex.shapes[0].expression.expressions[0].valueExpr, NodeConstraint
    )
    assert shex.shapes[0].expression.expressions[0].valueExpr.type == "NodeConstraint"
    assert shex.shapes[0].expression.expressions[0].valueExpr.nodeKind == "literal"

    assert shex.shapes[0].expression.expressions[1].type == "TripleConstraint"
    assert (
        shex.shapes[0].expression.expressions[1].predicate
        == "http://purl.org/dc/terms/description"
    )
    assert shex.shapes[0].expression.expressions[1].valueExpr.type == "NodeConstraint"
    assert (
        shex.shapes[0].expression.expressions[1].valueExpr.datatype
        == "http://www.w3.org/2001/XMLSchema#string"
    )

    assert shex.shapes[0].expression.expressions[2].type == "TripleConstraint"
    assert (
        shex.shapes[0].expression.expressions[2].predicate
        == "http://purl.org/dc/terms/subject"
    )
    assert shex.shapes[0].expression.expressions[2].valueExpr.type == "NodeConstraint"
    assert (
        shex.shapes[0].expression.expressions[2].valueExpr.values[0].type == "IriStem"
    )
    assert (
        shex.shapes[0].expression.expressions[2].valueExpr.values[0].stem
        == "http://lod.nal.usda.gov/nalt/"
    )

    assert shex.shapes[0].expression.expressions[3].type == "TripleConstraint"
    assert (
        shex.shapes[0].expression.expressions[3].predicate
        == "http://purl.org/dc/terms/creator"
    )
    assert (
        shex.shapes[0].expression.expressions[3].valueExpr
        == "http://example.org/mycreator"
    )


def test_shexj_from_file():
    """ Load ShEx JSON from internal file"""
    shex_file = os.path.join(EXAMPLE_PROFILES_DIRECTORY, "basic_profile.shexj")
    shex = SchemaLoader().load(shex_file)
    assert isinstance(shex.shapes[0].expression, EachOf)
    assert (
        TripleConstraint(
            predicate="http://purl.org/dc/terms/creator",
            valueExpr="http://example.org/mycreator",
        )
        in shex.shapes[0].expression.expressions
    )
    assert (
        TripleConstraint(
            predicate="http://purl.org/dc/terms/subject",
            valueExpr=NodeConstraint(
                values=[IriStem(stem="http://lod.nal.usda.gov/nalt/")]
            ),
        )
        in shex.shapes[0].expression.expressions
    )


def test_shexj_from_json():
    """ Load ShEx JSON from JSON file """
    shex = cast(
        ShExJ.Schema,
        loader.load(
            os.path.join(EXAMPLE_PROFILES_DIRECTORY, "basic_profile.shexj"),
            ShExJ,
        ),
    )
    assert isinstance(shex.shapes[0].expression, EachOf)
    assert (
        TripleConstraint(
            predicate="http://purl.org/dc/terms/subject",
            valueExpr=NodeConstraint(
                values=[IriStem(stem="http://lod.nal.usda.gov/nalt/")]
            ),
        )
        in shex.shapes[0].expression.expressions
    )
