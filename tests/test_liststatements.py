"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.csvparser import list_statements, Statement



def test_liststatements():
    """Turn list of dictionaries into list of Statement objects."""
    input = [
        {"shape_id": "@a", "prop_id": "dct:creator", "value_type": "URI"},
        {"shape_id": "@a", "prop_id": "dct:subject", "value_type": "URI"},
        {"shape_id": "@a", "prop_id": "dct:date", "value_type": "String"},
        {"shape_id": "@b", "prop_id": "foaf:name", "value_type": "String"},
    ]
    assert list_statements(input) == [
        Statement(shape_id="@a", prop_id="dct:creator", value_type="URI"),
        Statement(shape_id="@a", prop_id="dct:subject", value_type="URI"),
        Statement(shape_id="@a", prop_id="dct:date", value_type="String"),
        Statement(shape_id="@b", prop_id="foaf:name", value_type="String"),
    ]


def test_liststatements_without_shapeids():
    """Not shape IDs specified, so shape is '@default'."""
    input = [
        {"shape_id": None, "prop_id": "dct:creator", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:subject", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:date", "value_type": "String"},
    ]
    assert list_statements(input) == [
        Statement(shape_id='@default', prop_id="dct:creator", value_type="URI"),
        Statement(shape_id='@default', prop_id="dct:subject", value_type="URI"),
        Statement(shape_id='@default', prop_id="dct:date", value_type="String"),
    ]


def test_liststatements_with_shape_in_first_statement_only():
    """Shape IDs from previous statements added to statements without Shape IDs."""
    input = [
        {"shape_id": "@a", "prop_id": "dct:creator", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:subject", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:date", "value_type": "String"},
    ]
    assert list_statements(input) == [
        Statement(shape_id='@a', prop_id="dct:creator", value_type="URI"),
        Statement(shape_id='@a', prop_id="dct:subject", value_type="URI"),
        Statement(shape_id='@a', prop_id="dct:date", value_type="String"),
    ]


