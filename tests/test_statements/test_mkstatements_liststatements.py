"""Use list of dictionaries to initialize list of Statement objects."""

from csv2shex.mkstatements import list_statements, Statement


def test_liststatements():
    """Turn list of dictionaries into list of Statement objects."""
    csvrows_list = [
        {"shapeID": "@a", "prop_id": "dct:creator", "value_node_type": "URI"},
        {"shapeID": "@a", "prop_id": "dct:subject", "value_node_type": "URI"},
        {"shapeID": "@a", "prop_id": "dct:date", "value_node_type": "String"},
        {"shapeID": "@b", "prop_id": "foaf:name", "value_node_type": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", prop_id="dct:creator", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", prop_id="dct:subject", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", prop_id="dct:date", value_node_type="String"
        ),
        Statement(
            start=False, shapeID="@b", prop_id="foaf:name", value_node_type="String"
        ),
    ]


def test_liststatements_without_shapeIDs():
    """Not shape IDs specified, so shape is '@default'."""
    csvrows_list = [
        {"prop_id": "dct:creator", "value_node_type": "URI"},
        {"prop_id": "dct:subject", "value_node_type": "URI"},
        {"prop_id": "dct:date", "value_node_type": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True,
            shapeID="@default",
            prop_id="dct:creator",
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            prop_id="dct:subject",
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            prop_id="dct:date",
            value_node_type="String",
        ),
    ]


def test_liststatements_with_shapeIDs_specified_as_none():
    """Shape IDs specified as 'None', so shape is '@default'.
    When "shapeID" specified as 'None', row["shapeID"] will be False.
    General case: when field specified as None."""
    csvrows_list = [
        {"shapeID": None, "prop_id": "dct:creator", "value_node_type": "URI"},
        {"shapeID": None, "prop_id": "dct:subject", "value_node_type": "URI"},
        {"shapeID": None, "prop_id": "dct:date", "value_node_type": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True,
            shapeID="@default",
            prop_id="dct:creator",
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            prop_id="dct:subject",
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            prop_id="dct:date",
            value_node_type="String",
        ),
    ]


def test_liststatements_with_shape_in_first_statement_only():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    csvrows_list = [
        {"shapeID": "@a", "prop_id": "dct:creator", "value_node_type": "URI"},
        {"shapeID": None, "prop_id": "dct:subject", "value_node_type": "URI"},
        {"shapeID": None, "prop_id": "dct:date", "value_node_type": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", prop_id="dct:creator", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", prop_id="dct:subject", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", prop_id="dct:date", value_node_type="String"
        ),
    ]


def test_liststatements_with_shape_on_its_own_line():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    csvrows_list = [
        {"shapeID": "@a", "prop_id": None, "value_node_type": None},
        {"shapeID": None, "prop_id": "dct:creator", "value_node_type": "URI"},
        {"shapeID": None, "prop_id": "dct:subject", "value_node_type": "URI"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", prop_id="dct:creator", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", prop_id="dct:subject", value_node_type="URI"
        ),
    ]


def test_liststatements_with_shape_on_its_own_line_fields_with_none_are_implicit():
    """Fields with value None (here: 'note' and 'start') are simply implicit."""
    csvrows_list = [
        {"shapeID": "@a", "prop_id": None, "value_node_type": None},
        {"shapeID": None, "prop_id": "dct:creator", "value_node_type": "URI"},
        {"shapeID": None, "prop_id": "dct:subject", "value_node_type": "URI"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True,
            shapeID="@a",
            prop_id="dct:creator",
            note=None,
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@a",
            prop_id="dct:subject",
            prop_label=None,
            value_node_type="URI",
        ),
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", prop_id="dct:creator", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", prop_id="dct:subject", value_node_type="URI"
        ),
    ]


def test_liststatements_with_missing_value_node_type():
    """Should parse even if input lacks field 'value_node_type'."""
    as_input = [
        {
            "shapeID": "@book",
            "prop_id": "",
            "prop_label": "Book",
            "value_constraint": "",
            "note": "",
        },
        {
            "shapeID": "",
            "prop_id": "rdf:type",
            "prop_label": "instance of",
            "value_constraint": "sdo:Book",
            "note": "must be schema.org/Book",
        },
        {
            "shapeID": "",
            "prop_id": "rdf:type",
            "prop_label": "instance of",
            "value_constraint": "wd:Q571",
            "note": "must be wikidata Book",
        },
    ]
    expected = [
        Statement(
            start=True,
            shapeID="@book",
            shapeLabel=None,
            prop_id="rdf:type",
            prop_label="instance of",
            mand=False,
            repeat=False,
            value_node_type=None,
            value_constraint="sdo:Book",
            value_constraint_type=None,
            value_shape=None,
            note="must be schema.org/Book",
        ),
        Statement(
            start=True,
            shapeID="@book",
            shapeLabel=None,
            prop_id="rdf:type",
            prop_label="instance of",
            mand=False,
            repeat=False,
            value_node_type=None,
            value_constraint="wd:Q571",
            value_constraint_type=None,
            value_shape=None,
            note="must be wikidata Book",
        ),
    ]
    assert list_statements(as_input) == expected
