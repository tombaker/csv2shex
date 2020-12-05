"""Pretty-print csvshape dicts to console."""

import pytest
from dataclasses import asdict
from textwrap import dedent
from csv2shex.csvshape import CSVShape, CSVTripleConstraint
from csv2shex.inspect import pprint_csvshapes
from csv2shex.csvreader import _get_csvshapes

SHAPES_LIST = [
    CSVShape(
        shapeID=":a",
        shapeLabel=None,
        start=True,
        shapeClosed=False,
        tc_list=[
            CSVTripleConstraint(
                propertyID="dct:creator",
                mandatory=False,
                note=None,
                propertyLabel=None,
                repeatable=False,
                valueConstraint=None,
                valueConstraintType=None,
                valueDataType=None,
                valueNodeType=None,
                valueShape=None,
            ), CSVTripleConstraint(
                propertyID="dct:date",
                mandatory=False,
                note=None,
                propertyLabel=None,
                repeatable=False,
                valueConstraint=None,
                valueConstraintType=None,
                valueDataType=None,
                valueNodeType=None,
                valueShape=None,
            ),
        ],
    ), 
    CSVShape(
        shapeID=":b",
        shapeLabel=None,
        start=False,
        shapeClosed=False,
        tc_list=[
            CSVTripleConstraint(
                propertyID="foaf:name",
                mandatory=False,
                note=None,
                propertyLabel=None,
                repeatable=False,
                valueConstraint=None,
                valueConstraintType=None,
                valueDataType=None,
                valueNodeType=None,
                valueShape=None,
            )
        ],
    ),
]

def test_get_csvshape_dicts_list_two_shapes():
    """Turn list of CSVRow objects into list with two csvshape dicts."""
    expected_output_dedented = dedent(
        """\
    DC Tabular Application Profile
        Shape
            shapeID: :a
            start: True
            Triple Constraint
                propertyID: dct:creator
            Triple Constraint
                propertyID: dct:date
        Shape
            shapeID: :b
            Triple Constraint
                propertyID: foaf:name
    """
    )
    assert pprint_csvshapes(SHAPES_LIST) == expected_output_dedented.splitlines()


def test_get_csvshape_dicts_list_two_shapes_verbose():
    """Turn list of CSVRow objects into list with two CSVShapes."""
    expected_output_dedented = dedent(
        """\
    DC Tabular Application Profile
        Shape
            shapeID: :a
            shapeLabel: None
            shapeClosed: False
            start: True
            Triple Constraint
                propertyID: dct:creator
                propertyLabel: None
                mandatory: False
                repeatable: False
                valueNodeType: None
                valueDataType: None
                valueConstraint: None
                valueConstraintType: None
                valueShape: None
                note: None
            Triple Constraint
                propertyID: dct:date
                propertyLabel: None
                mandatory: False
                repeatable: False
                valueNodeType: None
                valueDataType: None
                valueConstraint: None
                valueConstraintType: None
                valueShape: None
                note: None
        Shape
            shapeID: :b
            shapeLabel: None
            shapeClosed: False
            start: False
            Triple Constraint
                propertyID: foaf:name
                propertyLabel: None
                mandatory: False
                repeatable: False
                valueNodeType: None
                valueDataType: None
                valueConstraint: None
                valueConstraintType: None
                valueShape: None
                note: None
    """
    )
    assert (
        pprint_csvshapes(SHAPES_LIST, verbose=True)
        == expected_output_dedented.splitlines()
    )
