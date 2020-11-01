"""Pretty-print CSVShape objects to console."""

import pytest
from textwrap import dedent
from csv2shex.csvshapes import pprint_schema, list_csvshapeobjs, CSVShape
from csv2shex.csvrows import CSVRow


def test_list_csvshapeobjs_two_shapes():
    """Turn list of CSVRow objects into list with two CSVShapes."""
    csvshapes_list = [
        CSVShape(
            start=True,
            shapeID=":a",
            shapeLabel=None,
            shapeClosed=False,
            statement_csvrows_list=[
                {
                    "propertyID": "dct:creator",
                    "mandatory": False,
                    "note": None,
                    "propertyLabel": None,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueDataType": None,
                    "valueNodeType": None,
                    "valueShape": None,
                },
                {
                    "propertyID": "dct:date",
                    "mandatory": False,
                    "note": None,
                    "propertyLabel": None,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueDataType": None,
                    "valueNodeType": None,
                    "valueShape": None,
                },
            ],
        ),
        CSVShape(
            start=False,
            shapeID=":b",
            shapeLabel=None,
            statement_csvrows_list=[
                {
                    "propertyID": "foaf:name",
                    "mandatory": False,
                    "note": None,
                    "propertyLabel": None,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueDataType": None,
                    "valueNodeType": None,
                    "valueShape": None,
                }
            ],
        ),
    ]
    expected_output_indented = """\
    DCAP
        Shape
            shapeID: :a
            start: True
            Statement
                propertyID: dct:creator
            Statement
                propertyID: dct:date
        Shape
            shapeID: :b
            Statement
                propertyID: foaf:name
    """
    assert (
        pprint_schema(csvshapes_list) == dedent(expected_output_indented).splitlines()
    )


def test_list_csvshapeobjs_two_shapes_verbose():
    """Turn list of CSVRow objects into list with two CSVShapes."""
    csvshapes_list = [
        CSVShape(
            shapeID=":a",
            shapeLabel=None,
            shapeClosed=False,
            start=True,
            statement_csvrows_list=[
                {
                    "propertyID": "dct:creator",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": None,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "dct:date",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": None,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
            ],
        ),
        CSVShape(
            shapeID=":b",
            shapeLabel=None,
            shapeClosed=False,
            start=False,
            statement_csvrows_list=[
                {
                    "propertyID": "foaf:name",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": None,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                }
            ],
        ),
    ]
    expected_output_indented = """\
    DCAP
        Shape
            shapeID: :a
            shapeLabel: None
            shapeClosed: False
            start: True
            Statement
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
            Statement
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
            Statement
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
    assert (
        pprint_schema(csvshapes_list, verbose=True)
        == dedent(expected_output_indented).splitlines()
    )
