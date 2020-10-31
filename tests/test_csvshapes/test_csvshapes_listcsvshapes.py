"""Turn list of CSVRows into list of CSVShapes."""

import pytest
from csv2shex.csvshapes import pprint_shapes, list_csvshapes, CSVShape
from csv2shex.csvrows import CSVRow


@pytest.mark.start
@pytest.mark.skip
def test_listshapes_two_shapes():
    """Turn list of CSVRow objects into list with two CSVShapes."""
    list_of_csvrow_objects = [
        CSVRow(shapeID=":a", propertyID="dct:creator"),
        CSVRow(shapeID=":b", propertyID="foaf:name"),
    ]

    expected_list_of_csvshape_objects = [
        CSVShape(
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
        CSVShape(
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
    assert list_csvshapes(list_of_csvrow_objects) == expected_list_of_csvshape_objects


@pytest.mark.start
@pytest.mark.skip
def test_listshapes_one_shape():
    """Turn list of CSVRow objects into list with one CSVShape."""
    list_of_statements = [
        CSVRow(shapeID=":a", propertyID="dct:creator"),
        CSVRow(shapeID=":a", propertyID="dct:date"),
    ]

    expected_list_of_shape_objects = [
        CSVShape(
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
    assert list_csvshapes(list_of_statements) == expected_list_of_shape_objects


@pytest.mark.start
@pytest.mark.skip
def test_listshapes_one_shape_and_shapeLabel():
    """One CSVShape with shape label."""
    list_of_statements = [
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

    list_of_shapes = [
        CSVShape(
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
    assert list_csvshapes(list_of_statements) == list_of_shapes 


@pytest.mark.start
@pytest.mark.skip
def test_listshapes_two_shapes_assign_start_to_first():
    """First shape created is marked as the 'start' shape."""
    list_of_statement_objects = [
        CSVRow(shapeID=":a", shapeLabel="A CSVShape", propertyID=":prop1"),
        CSVRow(shapeID=":a", shapeLabel="A CSVShape", propertyID=":prop2"),
        CSVRow(shapeID=":b", shapeLabel="B CSVShape", propertyID=":prop3"),
    ]
    list_of_shape_objects = [
        CSVShape(
            start=True,
            shapeID=":a",
            shapeLabel="A CSVShape",
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
        CSVShape(
            start=False,
            shapeID=":b",
            shapeLabel="B CSVShape",
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
    #pprint(list_csvshapes(list_of_statement_objects))
    #print("")
    #pprint(list_of_shape_objects)
    #assert False
    assert list_csvshapes(list_of_statement_objects) == list_of_shape_objects
