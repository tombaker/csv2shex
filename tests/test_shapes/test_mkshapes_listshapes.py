"""Turn list of Statements into list of Shapes."""

import pytest
from csv2shex.mkshapes import list_shapes, Shape
from csv2shex.mkstatements import Statement



def test_listshapes_one_shape():
    """Turn list of Statement objects into list with one Shape."""
    as_input = [
        Statement(
            start=True, shapeID=":a", propertyID="dct:creator", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID=":a", propertyID="dct:date", valueNodeType="String"
        ),
    ]
    assert list_shapes(as_input) == [
        Shape(
            start=True,
            shapeID=":a",
            shapeLabel=None,
            shape_statements=[
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
        )
    ]


def test_listshapes_one_shape_and_shapeLabel():
    """One Shape with shape label."""
    as_input = [
        Statement(
            start=True,
            shapeID=":a",
            shapeLabel="Author",
            propertyID="dct:creator",
            valueNodeType="URI",
        ),
        Statement(
            start=True,
            shapeID=":a",
            shapeLabel="Author",
            propertyID="dct:date",
            valueNodeType="String",
        ),
    ]
    assert list_shapes(as_input) == [
        Shape(
            start=True,
            shapeID=":a",
            shapeLabel="Author",
            shape_statements=[
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
        )
    ]


def test_listshapes_two_shapes():
    """Turn list of Statement objects into list with two Shapes."""
    list_of_statement_objects = [
        Statement(
            start=True, shapeID=":a", propertyID="dct:creator", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID=":a", propertyID="dct:subject", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID=":a", propertyID="dct:date", valueNodeType="String"
        ),
        Statement(
            start=False, shapeID=":b", propertyID="foaf:name", valueNodeType="String"
        ),
    ]
    assert list_shapes(list_of_statement_objects) == [
        Shape(
            start=True,
            shapeID=":a",
            shape_statements=[
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
                    "propertyID": "dct:subject",
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
        ),
        Shape(
            start=False,
            shapeID=":b",
            shape_statements=[
                {
                    "propertyID": "foaf:name",
                    "valueNodeType": "String",
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
        ),
    ]


@pytest.mark.skip
def test_listshapes_two_shapes_assign_start_to_first():
    """First shape created is marked as the 'start' shape."""
    list_of_statement_objects = [
        Statement(shapeID=":a", shapeLabel="A Shape", propertyID=":prop1"),
        Statement(shapeID=":a", shapeLabel="A Shape", propertyID=":prop2"),
        Statement(shapeID=":b", shapeLabel="B Shape", propertyID=":prop3"),
    ]
    list_of_shape_objects = [
        Shape(
            start=True,
            shapeID=":a",
            shapeLabel="A Shape",
            shape_statements=[
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
        ),
        Shape(
            start=False,
            shapeID=":b",
            shapeLabel="B Shape",
            shape_statements=[
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
        ),
    ]
    #from pprint import pprint
    #pprint(list_shapes(list_of_statement_objects))
    #print("")
    #pprint(list_of_shape_objects)
    #assert False
    assert list_shapes(list_of_statement_objects) == list_of_shape_objects
