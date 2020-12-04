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


@pytest.mark.skip
def test_mkshex_mkshex_one_shape():
    """@@@"""
    input_csvshape = CSVShape(
        start=True,
        shapeID=":a",
        tc_list=[
            CSVTripleConstraint(propertyID="dct:creator", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="dct:subject", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="dct:date", valueNodeType="String"),
        ],
    )

    # fmt: off
    output_shexjsg_shape = Schema(
            _context=<pyjsg.jsglib.jsg_context.JSGContext object at 0x10f67e400>, 
            type='Schema', 
            imports=None, 
            startActs=None, 
            start=':a', 
            shapes=[
                Shape(
                    _context=<pyjsg.jsglib.jsg_context.JSGContext object at 0x10f67e400>, 
                    type='Shape', 
                    id=':a', 
                    extends=None, 
                    closed=None, 
                    extra=None, 
                    expression=EachOf(
                        _context=<pyjsg.jsglib.jsg_context.JSGContext object at 0x10f67e400>, 
                        type='EachOf', 
                        id=None, 
                        expressions=[
                            TripleConstraint(
                                _context=<pyjsg.jsglib.jsg_context.JSGContext object at 0x10f67e400>, 
                                type='TripleConstraint', 
                                id=None, 
                                inverse=None, 
                                predicate='dct:creator', 
                                valueExpr=NodeConstraint(
                                    _context=<pyjsg.jsglib.jsg_context.JSGContext object at 0x10f67e400>, 
                                    type='NodeConstraint', 
                                    id=None, 
                                    nodeKind='iri', 
                                    datatype=None, 
                                    values=None
                                ), 
                                min=0, 
                                max=1, 
                                onShapeExpression=None, 
                                semActs=None, 
                                annotations=None
                            ), TripleConstraint(
                                _context=<pyjsg.jsglib.jsg_context.JSGContext object at 0x10f67e400>, 
                                type='TripleConstraint', 
                                id=None, 
                                inverse=None, 
                                predicate='dct:subject', 
                                valueExpr=NodeConstraint(
                                    _context=<pyjsg.jsglib.jsg_context.JSGContext object at 0x10f67e400>, 
                                    type='NodeConstraint', 
                                    id=None, 
                                    nodeKind='iri', 
                                    datatype=None, 
                                    values=None
                                ), 
                                min=0, 
                                max=1, 
                                onShapeExpression=None, 
                                semActs=None, 
                                annotations=None
                            ), 
                            TripleConstraint(
                                _context=<pyjsg.jsglib.jsg_context.JSGContext object at 0x10f67e400>, 
                                type='TripleConstraint', 
                                id=None, 
                                inverse=None, 
                                predicate='dct:date', 
                                valueExpr=NodeConstraint(
                                    _context=<pyjsg.jsglib.jsg_context.JSGContext object at 0x10f67e400>, 
                                    type='NodeConstraint', 
                                    id=None, 
                                    nodeKind='literal', 
                                    datatype=None, 
                                    values=None
                                ), 
                                min=0, 
                                max=1, 
                                onShapeExpression=None, 
                                semActs=None, 
                                annotations=None
                            )
                        ], 
                        min=None, 
                        max=None, 
                        semActs=None, 
                        annotations=None
                     ), 
                     semActs=None, 
                     annotations=None
                )
            ], 
            **{'@context': 'http://www.w3.org/ns/shex.jsonld'}
        )
    # fmt: on
    assert mkshex(input_csvshape) == output_shexjsg_shape
