import os

from ShExJSG import ShExC
from ShExJSG.ShExJ import EachOf, TripleConstraint
from pyshex.utils.schema_loader import SchemaLoader
from rdflib import DCTERMS

from tests import EXAMPLE_PROFILES_DIRECTORY


def test_shexc_from_text():
    """ Load ShExC text string """
    shex_text = """PREFIX dct: <http://purl.org/dc/terms/>

    <default> {
        dct:title . ;
        dct:subject . ;
        dct:date .
    }"""

    shex = SchemaLoader().loads(shex_text)
    assert isinstance(shex.shapes[0].expression, EachOf)
    assert (
        TripleConstraint(predicate=DCTERMS.title)
        in shex.shapes[0].expression.expressions
    )


def test_shexc_from_file():
    """ Load ShExC from internal file"""
    shex_file = os.path.join(
        EXAMPLE_PROFILES_DIRECTORY, "absolute_minimal_profile.shexc"
    )
    shex = SchemaLoader().load(shex_file)
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
