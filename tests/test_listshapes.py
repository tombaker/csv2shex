"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.csvparser import list_shapes, Statement, Shape

LIST_OF_STATEMENT_OBJECTS = [
    Statement(shape_id="@photo", prop_id="dct:creator", value_type="URI"),
    Statement(shape_id="@photo", prop_id="dct:subject", value_type="URI"),
    Statement(shape_id="@photo", prop_id="dct:date", value_type="String"),
    Statement(shape_id="@photographer", prop_id="foaf:name", value_type="String"),
]


def test_listshapes():
    """Turn list of Statement objects into list of Shapes."""
    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
        Shape(
            {
                "@photo": [
                    {"start_shape": True},
                    {"prop_id": "dct:creator", "value_type": "URI"},
                    {"prop_id": "dct:subject", "value_type": "URI"},
                    {"prop_id": "dct:date", "value_type": "String"},
                ],
                "@photographer": [
                    {"start_shape": False},
                    {"prop_id": "foaf:name", "value_type": "String"},
                ],
            }
        )
    ]
