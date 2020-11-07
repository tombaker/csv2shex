"""Turn list of CSVRows into list of CSVShapes."""

import pytest
from pprint import pprint
from dataclasses import asdict
from csv2shex.csvshapes import CSVShape
from csv2shex.csvrow import CSVRow
from csv2shex.readwrite import get_csvshape_dicts_list


def test_get_csvshape_dicts_list_one_shape():
    """Turn list of CSVRow objects into list with one CSVShape."""
    csvrows_list = [
        CSVRow(shapeID=":a", propertyID="dct:creator"),
        CSVRow(shapeID=":a", propertyID="dct:date"),
    ]

    expected_csvshape_dicts_list = [
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
        }
    ]
    assert get_csvshape_dicts_list(csvrows_list) == expected_csvshape_dicts_list


def test_get_csvshape_dicts_list_two_shapes():
    """Turn list of CSVRow objects into list with two CSVShapes."""
    csvrows_list = [
        CSVRow(shapeID=":a", propertyID="dct:creator"),
        CSVRow(shapeID=":a", propertyID="dct:date"),
        CSVRow(shapeID=":b", propertyID="foaf:name"),
    ]

    expected_csvshape_dicts_list = [
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
    assert len(get_csvshape_dicts_list(csvrows_list)) == len(expected_csvshape_dicts_list)
    assert (
        get_csvshape_dicts_list(csvrows_list)[0]["statement_csvrows_list"]
        == expected_csvshape_dicts_list[0]["statement_csvrows_list"]
    )
    assert get_csvshape_dicts_list(csvrows_list) == expected_csvshape_dicts_list


def test_get_csvshape_dicts_list_one_shape_and_shapeLabel():
    """One CSVShape with shape label."""
    csvrows_list = [
        CSVRow(
            shapeID=":a",
            shapeLabel="Author",
            propertyID="dct:creator",
            valueNodeType="URI",
        ),
        CSVRow(
            shapeID=":a",
            shapeLabel="Author",
            propertyID="dct:date",
            valueNodeType="String",
        ),
    ]

    csvshape_dicts_list = [
        {
            "shapeID": ":a",
            "shapeLabel": "Author",
            "start": True,
            "shapeClosed": False,
            "statement_csvrows_list": [
                {
                    "propertyID": "dct:creator",
                    "valueNodeType": "URI",
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "dct:date",
                    "valueNodeType": "String",
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
            ],
        }
    ]
    assert get_csvshape_dicts_list(csvrows_list) == csvshape_dicts_list


def test_get_csvshape_dicts_list_two_shapes_assign_start_to_first():
    """First shape created is marked as the 'start' shape."""
    csvrows_list = [
        CSVRow(shapeID=":a", shapeLabel="A CSVShape", propertyID=":prop1"),
        CSVRow(shapeID=":a", shapeLabel="A CSVShape", propertyID=":prop2"),
        CSVRow(shapeID=":b", shapeLabel="B CSVShape", propertyID=":prop3"),
    ]
    csvshape_dicts_list = [
        {
            "shapeID": ":a",
            "shapeLabel": "A CSVShape",
            "start": True,
            "shapeClosed": False,
            "statement_csvrows_list": [
                {
                    "propertyID": ":prop1",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": ":prop2",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
            ],
        },
        {
            "shapeID": ":b",
            "shapeLabel": "B CSVShape",
            "start": False,
            "shapeClosed": False,
            "statement_csvrows_list": [
                {
                    "propertyID": ":prop3",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                }
            ],
        },
    ]
    assert get_csvshape_dicts_list(csvrows_list) == csvshape_dicts_list


def test_listshapes_one_shape_for_shex_example():
    """Turn list of CSVRow objects into list with one CSVShape."""
    csvrows_list = [
        CSVRow(
            shapeID="http://example.org/myshape",
            propertyID="http://purl.org/dc/terms/title",
            mandatory=True,
            repeatable=False,
            valueNodeType="literal",
            valueDataType=None,
            valueConstraint=None,
            valueConstraintType=None,
            valueShape=None,
        ),
        CSVRow(
            shapeID="http://example.org/myshape",
            propertyID="http://purl.org/dc/terms/description",
            mandatory=False,
            repeatable=False,
            valueNodeType=None,
            valueDataType="http://www.w3.org/2001/XMLSchema#string",
            valueConstraint=None,
            valueConstraintType=None,
            valueShape=None,
        ),
        CSVRow(
            shapeID="http://example.org/myshape",
            propertyID="http://purl.org/dc/terms/subject",
            mandatory=False,
            repeatable=False,
            valueNodeType=None,
            valueDataType=None,
            valueConstraint="http://lod.nal.usda.gov/nalt/",
            valueConstraintType="IriStem",
            valueShape=None,
        ),
        CSVRow(
            shapeID="http://example.org/myshape",
            propertyID="http://purl.org/dc/terms/creator",
            mandatory=False,
            repeatable=False,
            valueNodeType=None,
            valueDataType=None,
            valueConstraint=None,
            valueConstraintType=None,
            valueShape="http://example.org/mycreator",
        ),
    ]

    one_shape_with_csvrows_list = [
        {
            "shapeID": "http://example.org/myshape",
            "shapeLabel": None,
            "start": True,
            "shapeClosed": False,
            "statement_csvrows_list": [
                {
                    "propertyID": "http://purl.org/dc/terms/title",
                    "propertyLabel": None,
                    "mandatory": True,
                    "repeatable": False,
                    "valueNodeType": "literal",
                    "valueDataType": None,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "http://purl.org/dc/terms/description",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": "http://www.w3.org/2001/XMLSchema#string",
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "http://purl.org/dc/terms/subject",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": None,
                    "valueConstraint": "http://lod.nal.usda.gov/nalt/",
                    "valueConstraintType": "IriStem",
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "http://purl.org/dc/terms/creator",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": None,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": "http://example.org/mycreator",
                    "note": None,
                },
            ],
        }
    ]
    assert get_csvshape_dicts_list(csvrows_list) == one_shape_with_csvrows_list
