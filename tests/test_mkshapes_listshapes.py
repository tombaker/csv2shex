"""Turn list of Statements into list of Shapes."""

from csv2shex.mkshapes import list_shapes, Shape
from csv2shex.mkstatements import Statement

LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:subject", value_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:date", value_type="String"),
    Statement(start=False, shape_id="@b", prop_id="foaf:name", value_type="String"),
]


def test_listshapes_one_shape():
    """Turn list of Statement objects into list with one Shape."""
    as_input = [
        Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
        Statement(start=True, shape_id="@a", prop_id="dct:date", value_type="String"),
    ]
    assert list_shapes(as_input) == [
        Shape(
            start=True,
            shape_id="@a",
            shape_label=None,
            shape_statements=[
                {
                    "prop_id": "dct:creator",
                    "value_type": "URI",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                },
                {
                    "prop_id": "dct:date",
                    "value_type": "String",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                },
            ],
        )
    ]


def test_listshapes_one_shape_and_shape_label():
    """One Shape with shape label."""
    as_input = [
        Statement(
            start=True,
            shape_id="@a",
            shape_label="Author",
            prop_id="dct:creator",
            value_type="URI",
        ),
        Statement(
            start=True,
            shape_id="@a",
            shape_label="Author",
            prop_id="dct:date",
            value_type="String",
        ),
    ]
    assert list_shapes(as_input) == [
        Shape(
            start=True,
            shape_id="@a",
            shape_label="Author",
            shape_statements=[
                {
                    "prop_id": "dct:creator",
                    "value_type": "URI",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                },
                {
                    "prop_id": "dct:date",
                    "value_type": "String",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                },
            ],
        )
    ]


def test_listshapes_two_shapes():
    """Turn list of Statement objects into list with two Shapes."""
    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
        Shape(
            start=True,
            shape_id="@a",
            shape_statements=[
                {
                    "prop_id": "dct:creator",
                    "value_type": "URI",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                },
                {
                    "prop_id": "dct:subject",
                    "value_type": "URI",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                },
                {
                    "prop_id": "dct:date",
                    "value_type": "String",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                },
            ],
        ),
        Shape(
            start=False,
            shape_id="@b",
            shape_statements=[
                {
                    "prop_id": "foaf:name",
                    "value_type": "String",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                }
            ],
        ),
    ]
