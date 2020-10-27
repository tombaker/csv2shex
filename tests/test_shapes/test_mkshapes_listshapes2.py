"""Turn list of Statements into list of Shapes (for ShEx example)."""

from csv2shex.mkshapes import list_shapes, Shape
from csv2shex.mkstatements import Statement
from pprint import pprint


def test_listshapes_one_shape_for_shex_example():
    """Turn list of Statement objects into list with one Shape."""
    list_of_statement_objects = [
        Statement(
            start=True, 
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
        Statement(
            start=True, 
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
        Statement(
            start=True, 
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
        Statement(
            start=True, 
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

    one_shape_with_list_of_statement_objects = [
        Shape(
            start=True,
            shapeID="http://example.org/myshape",
            shapeLabel=None,
            shape_statements=[
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
    assert list_shapes(list_of_statement_objects) == one_shape_with_list_of_statement_objects
