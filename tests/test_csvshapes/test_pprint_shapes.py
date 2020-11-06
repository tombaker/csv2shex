"""Pretty-print CSVShape objects to console."""

import pytest
from dataclasses import asdict
from textwrap import dedent
from csv2shex.csvshapes import pprint_schema, get_csvshapes_dict, CSVShape
from csv2shex.csvrows import CSVRow


def test_get_csvshapes_dict_two_shapes():
    """Turn list of CSVRow objects into list with two CSVShapes."""
    csvshape_dicts_list = [
        {
            "shapeID": ":a",
            "shapeLabel": None,
            "start": True,
            "shapeClosed": False,
            "statement_csvrows_list": [
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
        },
        {
            "shapeID": ":b",
            "shapeLabel": None,
            "start": False,
            "shapeClosed": False,
            "statement_csvrows_list": [
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
        },
    ]

    expected_output_dedented = dedent(
        """\
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
    )
    assert pprint_schema(csvshape_dicts_list) == expected_output_dedented.splitlines()


def test_get_csvshapes_dict_two_shapes_verbose():
    """Turn list of CSVRow objects into list with two CSVShapes."""
    csvshape_dicts_list = [
        {
            "shapeID": ":a",
            "shapeLabel": None,
            "start": True,
            "shapeClosed": False,
            "statement_csvrows_list": [
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
        },
        {
            "shapeID": ":b",
            "shapeLabel": None,
            "start": False,
            "shapeClosed": False,
            "statement_csvrows_list": [
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
        },
    ]

    expected_output_dedented = dedent(
        """\
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
    )
    assert (
        pprint_schema(csvshape_dicts_list, verbose=True)
        == expected_output_dedented.splitlines()
    )
