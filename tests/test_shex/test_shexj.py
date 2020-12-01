import os
from typing import cast
import pytest

from ShExJSG import ShExC, ShExJ
from ShExJSG.SchemaWithContext import Schema
from ShExJSG.ShExJ import Shape, EachOf, TripleConstraint
from pyjsg.jsglib import loader
from pyjsg.jsglib.loader import is_valid, StringIO
from pyshex.utils.schema_loader import SchemaLoader
from rdflib import DCTERMS

from tests import EXAMPLE_PROFILES_DIRECTORY


def test_shexj_from_text():
    """ Load ShEx JSON text string """
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


def test_shexj_from_file():
    """ Load ShEx JSON from internal file"""
    shex_file = os.path.join(
        EXAMPLE_PROFILES_DIRECTORY, "absolute_minimal_profile.shexj"
    )
    shex = SchemaLoader().load(shex_file)
    assert isinstance(shex.shapes[0].expression, EachOf)
    assert (
        TripleConstraint(predicate=DCTERMS.title)
        in shex.shapes[0].expression.expressions
    )


def test_shexj_from_json():
    """ Load ShEx JSON from JSON file """
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


def test_emit_shexc():
    """ Generate ShExC from internal representation """
    shex_file = os.path.join(
        EXAMPLE_PROFILES_DIRECTORY, "absolute_minimal_profile.shexc"
    )
    shex = SchemaLoader().load(shex_file)
    assert (
        """<default> {
    (  <http://purl.org/dc/terms/title> . ;
       <http://purl.org/dc/terms/subject> . ;
       <http://purl.org/dc/terms/date> .
    )
}"""
        == (str(ShExC(shex))).strip()
    )


def test_python_to_shex():
    """ Generate a new ShEx Schema from Python """
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
    """ Determine whether the particular bit of ShEx is valid """
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


@pytest.mark.skip
def test_is_valid_shex_error():
    """ Determine whether the particular bit of ShEx is valid """

    # If this only has one expression, it errors out while being built
    # There IS a way to turn checking off, but will have to find it
    schema = Schema(
        shapes=[
            Shape(
                id="default",
                expression=EachOf(
                    expressions=[
                        TripleConstraint(predicate=DCTERMS.title),
                        TripleConstraint(predicate=DCTERMS.subject),
                    ]
                ),
            )
        ]
    )

    # This should turn this into an invalid entry.
    # Not certain why it still isn't caught in the log
    schema.shapes[0].expression.expressions.pop()
    log = StringIO()
    rval = is_valid(schema, log)
    print(log.getvalue())
    assert not rval
