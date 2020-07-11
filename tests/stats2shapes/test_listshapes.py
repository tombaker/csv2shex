"""Turn list of Statements into list of Shapes."""

from csv2shex.stats2shapes import list_shapes, Shape
from csv2shex.csv2stats import Statement

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
            property_values=[
                {"prop_id": "dct:creator", "value_type": "URI"},
                {"prop_id": "dct:date", "value_type": "String"},
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
            property_values=[
                {"prop_id": "dct:creator", "value_type": "URI"},
                {"prop_id": "dct:date", "value_type": "String"},
            ],
        )
    ]


def test_listshapes_two_shapes():
    """Turn list of Statement objects into list with two Shapes."""
    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
        Shape(
            start=True,
            shape_id="@a",
            property_values=[
                {"prop_id": "dct:creator", "value_type": "URI"},
                {"prop_id": "dct:subject", "value_type": "URI"},
                {"prop_id": "dct:date", "value_type": "String"},
            ],
        ),
        Shape(
            start=False,
            shape_id="@b",
            property_values=[{"prop_id": "foaf:name", "value_type": "String"}],
        ),
    ]
