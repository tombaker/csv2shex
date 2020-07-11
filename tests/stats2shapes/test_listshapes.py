"""Turn list of Statements into list of Shapes."""

import os
import pytest
from pathlib import Path
from csv2shex.stats2shapes import list_shapes, Shape
from csv2shex.csv2stats import Statement
from dataclasses import asdict

MINIMAL_LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:date", value_type="String"),
]

LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:subject", value_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:date", value_type="String"),
    Statement(start=False, shape_id="@b", prop_id="foaf:name", value_type="String"),
]

LIST_OF_SHAPE_OBJECTS = [
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


def test_listshapes():
    """Turn list of Statement objects into list of Shapes."""
    assert list_shapes(MINIMAL_LIST_OF_STATEMENT_OBJECTS) == [
        Shape(
            start=True,
            shape_id="@a",
            property_values=[
                {"prop_id": "dct:creator", "value_type": "URI"},
                {"prop_id": "dct:date", "value_type": "String"},
            ],
        ),
    ]

#    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
#    Shape(start=True, shape_id="@a", property_values=[
#            {
#                "prop_id": "dct:creator",
#                "value_type": "URI",
#            },
#            {
#                "prop_id": "dct:subject",
#                "value_type": "URI",
#            },
#            {
#                "prop_id": "dct:date",
#                "value_type": "String",
#            }, 
#    ]),
#    Shape(shape_id="@b", start=False, property_values=[
#            {
#                "prop_id": "foaf:name",
#                "value_type": "String",
#            },
#    ])
#    ]
