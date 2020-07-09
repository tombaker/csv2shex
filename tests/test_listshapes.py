"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.csvparser import list_shapes, Statement, Shape

LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:subject", value_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:date", value_type="String"),
    Statement(start=False, shape_id="@b", prop_id="foaf:name", value_type="String"),
]


def test_listshapes():
    """Turn list of Statement objects into list of Shapes."""
    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
        Shape(
            {
                "@a": [
                    {"start": True},
                    {"prop_id": "dct:creator", "value_type": "URI"},
                    {"prop_id": "dct:subject", "value_type": "URI"},
                    {"prop_id": "dct:date", "value_type": "String"},
                ],
                "@b": [
                    {"start": False},
                    {"prop_id": "foaf:name", "value_type": "String"},
                ],
            }
        )
    ]
