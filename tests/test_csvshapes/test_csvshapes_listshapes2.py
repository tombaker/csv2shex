"""Turn list of CSVRows into list of CSVShapes (for ShEx example)."""

import pytest
from csv2shex.csvshapes import list_csvshapes, CSVShape
from csv2shex.csvrows import CSVRow
from pprint import pprint


@pytest.mark.start
@pytest.mark.skip
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
        CSVShape(
            start=True,
            shapeID="http://example.org/myshape",
            shapeLabel=None,
            statement_csvrows_list=[
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
        )
    ]
    assert list_csvshapes(csvrows_list) == one_shape_with_csvrows_list
