"""Turn list of Statements into list of Shapes."""

from csv2shex.mkshapes import list_shapes, Shape
from csv2shex.mkstatements import Statement

LIST_OF_STATEMENT_OBJECTS = [
    Statement(
        start=True, shapeID="@a", propertyID="dct:creator", valueNodeType="URI"
    ),
    Statement(
        start=True, shapeID="@a", propertyID="dct:subject", valueNodeType="URI"
    ),
    Statement(
        start=True, shapeID="@a", propertyID="dct:date", valueNodeType="String"
    ),
    Statement(
        start=False, shapeID="@b", propertyID="foaf:name", valueNodeType="String"
    ),
]


def test_listshapes_one_shape():
    """Turn list of Statement objects into list with one Shape."""
    as_input = [
        Statement(
            start=True, shapeID="@a", propertyID="dct:creator", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:date", valueNodeType="String"
        ),
    ]
    assert list_shapes(as_input) == [
        Shape(
            start=True,
            shapeID="@a",
            shapeLabel=None,
            shape_statements=[
                {
                    "propertyID": "dct:creator",
                    "valueNodeType": "URI",
                    "value_datatype": None,
                    "prop_label": None,
                    "mandatory": False,
                    "repeatable": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
                {
                    "propertyID": "dct:date",
                    "valueNodeType": "String",
                    "value_datatype": None,
                    "prop_label": None,
                    "mandatory": False,
                    "repeatable": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
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
            shapeID="@a",
            shapeLabel="Author",
            propertyID="dct:creator",
            valueNodeType="URI",
        ),
        Statement(
            start=True,
            shapeID="@a",
            shapeLabel="Author",
            propertyID="dct:date",
            valueNodeType="String",
        ),
    ]
    assert list_shapes(as_input) == [
        Shape(
            start=True,
            shapeID="@a",
            shapeLabel="Author",
            shape_statements=[
                {
                    "propertyID": "dct:creator",
                    "valueNodeType": "URI",
                    "value_datatype": None,
                    "prop_label": None,
                    "mandatory": False,
                    "repeatable": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
                {
                    "propertyID": "dct:date",
                    "valueNodeType": "String",
                    "value_datatype": None,
                    "prop_label": None,
                    "mandatory": False,
                    "repeatable": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
            ],
        )
    ]


def test_listshapes_two_shapes():
    """Turn list of Statement objects into list with two Shapes."""
    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
        Shape(
            start=True,
            shapeID="@a",
            shape_statements=[
                {
                    "propertyID": "dct:creator",
                    "valueNodeType": "URI",
                    "value_datatype": None,
                    "prop_label": None,
                    "mandatory": False,
                    "repeatable": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
                {
                    "propertyID": "dct:subject",
                    "valueNodeType": "URI",
                    "value_datatype": None,
                    "prop_label": None,
                    "mandatory": False,
                    "repeatable": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
                {
                    "propertyID": "dct:date",
                    "valueNodeType": "String",
                    "value_datatype": None,
                    "prop_label": None,
                    "mandatory": False,
                    "repeatable": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
            ],
        ),
        Shape(
            start=False,
            shapeID="@b",
            shape_statements=[
                {
                    "propertyID": "foaf:name",
                    "valueNodeType": "String",
                    "value_datatype": None,
                    "prop_label": None,
                    "mandatory": False,
                    "repeatable": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                }
            ],
        ),
    ]
