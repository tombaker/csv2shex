"""Use list of dictionaries to initialize list of Statement objects."""

from csv2shex.csv2stats import list_statements, Statement


def test_liststatements():
    """Turn list of dictionaries into list of Statement objects."""
    as_input = [
        {"shape_id": "@a", "prop_id": "dct:creator", "value_type": "URI"},
        {"shape_id": "@a", "prop_id": "dct:subject", "value_type": "URI"},
        {"shape_id": "@a", "prop_id": "dct:date", "value_type": "String"},
        {"shape_id": "@b", "prop_id": "foaf:name", "value_type": "String"},
    ]
    assert list_statements(as_input) == [
        Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
        Statement(start=True, shape_id="@a", prop_id="dct:subject", value_type="URI"),
        Statement(start=True, shape_id="@a", prop_id="dct:date", value_type="String"),
        Statement(start=False, shape_id="@b", prop_id="foaf:name", value_type="String"),
    ]


def test_liststatements_without_shape_ids():
    """Not shape IDs specified, so shape is '@default'."""
    as_input = [
        {"shape_id": None, "prop_id": "dct:creator", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:subject", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:date", "value_type": "String"},
    ]
    assert list_statements(as_input) == [
        Statement(
            start=True, shape_id="@default", prop_id="dct:creator", value_type="URI"
        ),
        Statement(
            start=True, shape_id="@default", prop_id="dct:subject", value_type="URI"
        ),
        Statement(
            start=True, shape_id="@default", prop_id="dct:date", value_type="String"
        ),
    ]


def test_liststatements_with_shape_in_first_statement_only():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    as_input = [
        {"shape_id": "@a", "prop_id": "dct:creator", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:subject", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:date", "value_type": "String"},
    ]
    assert list_statements(as_input) == [
        Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
        Statement(start=True, shape_id="@a", prop_id="dct:subject", value_type="URI"),
        Statement(start=True, shape_id="@a", prop_id="dct:date", value_type="String"),
    ]


def test_liststatements_with_shape_on_its_own_line():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    as_input = [
        {"shape_id": "@a", "prop_id": None, "value_type": None},
        {"shape_id": None, "prop_id": "dct:creator", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:subject", "value_type": "URI"},
    ]
    assert list_statements(as_input) == [
        Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
        Statement(start=True, shape_id="@a", prop_id="dct:subject", value_type="URI"),
    ]


def test_liststatements_with_shape_on_its_own_line_fields_with_none_are_implicit():
    """Fields with value None (here: 'annot' and 'start') are simply implicit."""
    as_input = [
        {"shape_id": "@a", "prop_id": None, "value_type": None},
        {"shape_id": None, "prop_id": "dct:creator", "value_type": "URI"},
        {"shape_id": None, "prop_id": "dct:subject", "value_type": "URI"},
    ]
    assert list_statements(as_input) == [
        Statement(
            start=True,
            shape_id="@a",
            prop_id="dct:creator",
            annot=None,
            value_type="URI",
        ),
        Statement(
            start=True,
            shape_id="@a",
            prop_id="dct:subject",
            prop_label=None,
            value_type="URI",
        ),
    ]
    assert list_statements(as_input) == [
        Statement(start=True, shape_id="@a", prop_id="dct:creator", value_type="URI"),
        Statement(start=True, shape_id="@a", prop_id="dct:subject", value_type="URI"),
    ]
