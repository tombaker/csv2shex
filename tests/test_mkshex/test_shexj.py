import os
import pytest
from typing import cast

from ShExJSG import ShExC, ShExJ
from ShExJSG.SchemaWithContext import Schema
from ShExJSG.ShExJ import Shape, EachOf, TripleConstraint
from pyjsg.jsglib import loader
from pyjsg.jsglib.loader import is_valid, StringIO
from pyshex.utils.schema_loader import SchemaLoader
from rdflib import DCTERMS

from tests import EXAMPLE_PROFILES_DIRECTORY


def test_load_shexj_as_text_string():
    """Load ShExJ as text string."""
    shex_json = """
    {
       "@context": "http://www.w3.org/ns/shex.jsonld",
       "type": "Schema",
       "shapes": [
          {
             "type": "Shape",
             "id": "default",
             "expression": {
                "type": "EachOf",
                "expressions": [
                   {
                      "type": "TripleConstraint",
                      "predicate": "http://purl.org/dc/terms/title"
                   },
                   {
                      "type": "TripleConstraint",
                      "predicate": "http://purl.org/dc/terms/subject"
                   },
                   {
                      "type": "TripleConstraint",
                      "predicate": "http://purl.org/dc/terms/date"
                   }
                ]
             }
          }
       ]
    }
    """
    shex = SchemaLoader().loads(shex_json)
    assert isinstance(shex.shapes[0].expression, EachOf)
    assert (
        TripleConstraint(predicate=DCTERMS.title)
        in shex.shapes[0].expression.expressions
    )


def test_load_shexj_from_shexj_file():
    """Load ShExJ from internal ShExJ file."""
    shex_file = os.path.join(
        EXAMPLE_PROFILES_DIRECTORY, "absolute_minimal_profile.shexj"
    )
    shex = SchemaLoader().load(shex_file)
    assert isinstance(shex.shapes[0].expression, EachOf)
    assert (
        TripleConstraint(predicate=DCTERMS.title)
        in shex.shapes[0].expression.expressions
    )


def test_load_shexj_from_json_file():
    """Load ShExJ from internal JSON file."""
    shex = cast(
        ShExJ.Schema,
        loader.load(
            os.path.join(EXAMPLE_PROFILES_DIRECTORY, "absolute_minimal_profile.shexj"),
            ShExJ,
        ),
    )
    assert isinstance(shex.shapes[0].expression, EachOf)
    assert (
        TripleConstraint(predicate=DCTERMS.title)
        in shex.shapes[0].expression.expressions
    )


def test_convert_shex_pyobj_to_shexc_string():
    """Generate a new ShEx Schema from Python object."""
    schema = Schema(
        shapes=[
            Shape(
                id="default",
                expression=EachOf(
                    expressions=[
                        TripleConstraint(predicate=DCTERMS.title),
                        TripleConstraint(predicate=DCTERMS.subject),
                        TripleConstraint(predicate=DCTERMS.date),
                    ]
                ),
            )
        ]
    )
    assert (
        """<default> {
    (  <http://purl.org/dc/terms/title> . ;
       <http://purl.org/dc/terms/subject> . ;
       <http://purl.org/dc/terms/date> .
    )
}"""
        == (str(ShExC(schema))).strip()
    )


def test_is_valid_shex_good():
    """Check whether Python object for ShEx is valid."""
    schema = Schema(
        shapes=[
            Shape(
                id="default",
                expression=EachOf(
                    expressions=[
                        TripleConstraint(predicate=DCTERMS.title),
                        TripleConstraint(predicate=DCTERMS.subject),
                        TripleConstraint(predicate=DCTERMS.date),
                    ]
                ),
            )
        ]
    )
    log = StringIO()
    rval = is_valid(schema, log)
    assert rval, log.getvalue()
