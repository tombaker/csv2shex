"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.csv2stats import list_statements, Statement



def test_liststatements():
    """Turn list of dictionaries into list of Statement objects."""
    input = [
        {"shapeid": "@a", "prop_id": "dct:creator", "v_type": "URI"},
        {"shapeid": "@a", "prop_id": "dct:subject", "v_type": "URI"},
        {"shapeid": "@a", "prop_id": "dct:date", "v_type": "String"},
        {"shapeid": "@b", "prop_id": "foaf:name", "v_type": "String"},
    ]
    assert list_statements(input) == [
        Statement(shapeid="@a", prop_id="dct:creator", v_type="URI"),
        Statement(shapeid="@a", prop_id="dct:subject", v_type="URI"),
        Statement(shapeid="@a", prop_id="dct:date", v_type="String"),
        Statement(shapeid="@b", prop_id="foaf:name", v_type="String"),
    ]


def test_liststatements_without_shapeids():
    """Not shape IDs specified, so shape is '@default'."""
    input = [
        {"shapeid": None, "prop_id": "dct:creator", "v_type": "URI"},
        {"shapeid": None, "prop_id": "dct:subject", "v_type": "URI"},
        {"shapeid": None, "prop_id": "dct:date", "v_type": "String"},
    ]
    assert list_statements(input) == [
        Statement(shapeid='@default', prop_id="dct:creator", v_type="URI"),
        Statement(shapeid='@default', prop_id="dct:subject", v_type="URI"),
        Statement(shapeid='@default', prop_id="dct:date", v_type="String"),
    ]


def test_liststatements_with_shape_in_first_statement_only():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    input = [
        {"shapeid": "@a", "prop_id": "dct:creator", "v_type": "URI"},
        {"shapeid": None, "prop_id": "dct:subject", "v_type": "URI"},
        {"shapeid": None, "prop_id": "dct:date", "v_type": "String"},
    ]
    assert list_statements(input) == [
        Statement(shapeid='@a', prop_id="dct:creator", v_type="URI"),
        Statement(shapeid='@a', prop_id="dct:subject", v_type="URI"),
        Statement(shapeid='@a', prop_id="dct:date", v_type="String"),
    ]


def test_liststatements_with_shape_on_its_own_line():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    input = [
        {"shapeid": "@a", "prop_id": None, "v_type": None},
        {"shapeid": None, "prop_id": "dct:creator", "v_type": "URI"},
        {"shapeid": None, "prop_id": "dct:subject", "v_type": "URI"},
    ]
    assert list_statements(input) == [
        Statement(shapeid='@a', prop_id="dct:creator", v_type="URI"),
        Statement(shapeid='@a', prop_id="dct:subject", v_type="URI"),
    ]


