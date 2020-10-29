"""Turn list of Statements into list of Shapes."""

import pytest
from csv2shex.mkshapes import pprint_shapes, list_shapes, Shape
from csv2shex.mkstatements import Statement


@pytest.mark.start
@pytest.mark.skip
def test_listshapes_two_shapes():
    """Turn list of Statement objects into list with two Shapes."""
    list_of_statement_objects = [
        Statement(shapeID=":a", propertyID="dct:creator"),
        Statement(shapeID=":b", propertyID="foaf:name"),
    ]

    expected_list_of_shape_objects = [
        Shape(
            start=True,
            shapeID=":a",
            shapeLabel=None,
            shape_statements=[
                {
                    "propertyID": "dct:creator",
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
            shapeLabel=None,
            shape_statements=[
                {
                    "propertyID": "foaf:name",
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
    assert list_shapes(list_of_statement_objects) == expected_list_of_shape_objects


@pytest.mark.start
@pytest.mark.skip
def test_listshapes_one_shape():
    """Turn list of Statement objects into list with one Shape."""
    list_of_statements = [
        Statement(shapeID=":a", propertyID="dct:creator"),
        Statement(shapeID=":a", propertyID="dct:date"),
    ]

    expected_list_of_shape_objects = [
        Shape(
            start=True,
            shapeID=":a",
            shapeLabel=None,
            shape_statements=[
                {
                    "propertyID": "dct:creator",
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
                    "propertyID": "dct:date",
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
        )
    ]
    assert list_shapes(list_of_statements) == expected_list_of_shape_objects


@pytest.mark.start
@pytest.mark.skip
def test_listshapes_one_shape_and_shapeLabel():
    """One Shape with shape label."""
    list_of_statements = [
        Statement(
            shapeID=":a",
            shapeLabel="Author",
            propertyID="dct:creator",
            valueNodeType="URI",
        ),
        Statement(
            shapeID=":a",
            shapeLabel="Author",
            propertyID="dct:date",
            valueNodeType="String",
        ),
    ]

    list_of_shapes = [
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
    assert list_shapes(list_of_statements) == list_of_shapes 


@pytest.mark.start
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
