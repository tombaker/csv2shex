"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.stats2shapes import list_shapes
from csv2shex.csv2stats import Statement
from dataclasses import asdict

LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:subject", value_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:date", value_type="String"),
    Statement(start=False, shape_id="@b", prop_id="foaf:name", value_type="String"),
]


def test_listshapes():
    """Turn list of Statement objects into list of Shapes."""
    pass
#    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == {
#        "@a": [{"start": True}, [
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
#        ]],
#        "@b": [{"start": False}, [
#            {
#                "prop_id": "foaf:name",
#                "value_type": "String",
#            }
#        ]],
#    }
#

# def test_prepare():
#     """Temporary throwaway test..."""
#     assert len(LIST_OF_STATEMENT_OBJECTS) == 4
#     assert LIST_OF_STATEMENT_OBJECTS == [s for s in LIST_OF_STATEMENT_OBJECTS]
#     assert [asdict(s) for s in LIST_OF_STATEMENT_OBJECTS] == [
#     {"start": True,  "shape_id": "@a", "prop_id": "dct:creator", "value_type": "URI"},
#     {"start": True,  "shape_id": "@a", "prop_id": "dct:subject", "value_type": "URI"},
#     {"start": True,  "shape_id": "@a", "prop_id": "dct:date", "value_type": "String"},
#     {"start": False, "shape_id": "@b", "prop_id": "foaf:name", "value_type": "String"},
#     ]
#     assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
#     {"start": True,  "shape_id": "@a", "prop_id": "dct:creator", "value_type": "URI"},
#     {"start": True,  "shape_id": "@a", "prop_id": "dct:subject", "value_type": "URI"},
#     {"start": True,  "shape_id": "@a", "prop_id": "dct:date", "value_type": "String"},
#     {"start": False, "shape_id": "@b", "prop_id": "foaf:name", "value_type": "String"},
#     ]
#
