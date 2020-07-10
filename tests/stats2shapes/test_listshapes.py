"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.stats2shapes import list_shapes
from csv2shex.csv2stats import Statement
from dataclasses import asdict

MINIMAL_LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shapeid="@a", prop_id="dct:creator", v_type="URI"),
    Statement(start=True, shapeid="@a", prop_id="dct:date", v_type="String"),
]

LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shapeid="@a", prop_id="dct:creator", v_type="URI"),
    Statement(start=True, shapeid="@a", prop_id="dct:subject", v_type="URI"),
    Statement(start=True, shapeid="@a", prop_id="dct:date", v_type="String"),
    Statement(start=False, shapeid="@b", prop_id="foaf:name", v_type="String"),
]


def test_listshapes():
    """Turn list of Statement objects into list of Shapes."""
    assert True

#    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
#    Shape(shapeid="@a", start=True, property_values=[
#            {
#                "prop_id": "dct:creator",
#                "v_type": "URI",
#            },
#            {
#                "prop_id": "dct:subject",
#                "v_type": "URI",
#            },
#            {
#                "prop_id": "dct:date",
#                "v_type": "String",
#            }, 
#    ]),
#    Shape(shapeid="@b", start=False, property_values=[
#            {
#                "prop_id": "foaf:name",
#                "v_type": "String",
#            },
#    ])
#    ]
