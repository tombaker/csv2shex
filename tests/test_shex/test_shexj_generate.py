import os
import pytest
from typing import cast

from ShExJSG import ShExC, ShExJ
from ShExJSG.SchemaWithContext import Schema
from ShExJSG.ShExJ import Shape, EachOf, TripleConstraint, NodeConstraint, IriStem
# from pyjsg.jsglib import loader
# from pyshex.utils.schema_loader import SchemaLoader
from pyjsg.jsglib.loader import is_valid, StringIO
from rdflib import DCTERMS

from tests import EXAMPLE_PROFILES_DIRECTORY

from pyjsg.jsglib.jsg_array import JSGArray


def test_python_to_shex():
    """ Generate a new ShEx Schema from Python """
    schema = Schema(
        shapes=[
            Shape(
                id="http://example.org/myshape",
                expression=EachOf(
                    expressions=[
                        TripleConstraint(
                            predicate=DCTERMS.title,
                            valueExpr=NodeConstraint(nodeKind="literal"),
                            min=1,
                            max=-1,
                        ),
                        TripleConstraint(
                            predicate=DCTERMS.description,
                            valueExpr=NodeConstraint(
                                datatype="http://www.w3.org/2001/XMLSchema#string"
                            ),
                        ),
                        TripleConstraint(
                            predicate=DCTERMS.subject,
                            valueExpr=NodeConstraint(
                                values=[IriStem(stem="http://lod.nal.usda.gov/nalt/")]
                            ),
                        ),
                        TripleConstraint(
                            predicate=DCTERMS.creator,
                            valueExpr="http://example.org/mycreator",
                        ),
                    ]
                ),
            )
        ]
    )
    assert (
        """<http://example.org/myshape> {
    (  <http://purl.org/dc/terms/title> LITERAL + ;
       <http://purl.org/dc/terms/description> <http://www.w3.org/2001/XMLSchema#string> ;
       <http://purl.org/dc/terms/subject> [ <http://lod.nal.usda.gov/nalt/>~ ] ;
       <http://purl.org/dc/terms/creator> @<http://example.org/mycreator>
    )
}"""
        == (str(ShExC(schema))).strip()
    )


def test_is_valid_shex_good():
    """Determine whether the particular bit of ShEx is valid.

    Is this testing whether it is valid as ShEx? In what sense?"""
    schema = Schema(
        shapes=[
            Shape(
                id="http://example.org/myshape",
                expression=EachOf(
                    expressions=[
                        TripleConstraint(
                            predicate=DCTERMS.title,
                            valueExpr=NodeConstraint(nodeKind="literal"),
                            min=1,
                            max=-1,
                        ),
                        TripleConstraint(
                            predicate=DCTERMS.description,
                            valueExpr=NodeConstraint(
                                datatype="http://www.w3.org/2001/XMLSchema#string"
                            ),
                        ),
                        TripleConstraint(
                            predicate=DCTERMS.subject,
                            valueExpr=NodeConstraint(
                                values=[IriStem(stem="http://lod.nal.usda.gov/nalt/")]
                            ),
                        ),
                        TripleConstraint(
                            predicate=DCTERMS.creator,
                            valueExpr="http://example.org/mycreator",
                        ),
                    ]
                ),
            )
        ]
    )
    log = StringIO()
    rval = is_valid(schema, log)
    assert rval, log.getvalue()

# @pytest.mark.skip
# def test_is_valid_shex_error():
#    """ Determine whether the particular bit of ShEx is valid """
#
#    # If this only has one expression, it errors out while being built
#    # There IS a way to turn checking off, but will have to find it
#    schema = Schema(
#        shapes=[
#            Shape(
#                id="default",
#                expression=EachOf(
#                    expressions=[
#                        TripleConstraint(predicate=DCTERMS.title),
#                        TripleConstraint(predicate=DCTERMS.subject),
#                    ]
#                ),
#            )
#        ]
#    )
#
#    # This should turn this into an invalid entry.
#    # Not certain why it still isn't caught in the log
#    schema.shapes[0].expression.expressions.pop()
#    log = StringIO()
#    rval = is_valid(schema, log)
#    print(log.getvalue())
#    assert not rval
