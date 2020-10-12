"""Use list of dictionaries to initialize list of Statement objects."""

from csv2shex.mkstatements import list_statements, Statement


def test_liststatements():
    """Turn list of dictionaries into list of Statement objects."""
    csvrows_list = [
        {"shapeID": "@a", "propertyID": "dct:creator", "value_node_type": "URI"},
        {"shapeID": "@a", "propertyID": "dct:subject", "value_node_type": "URI"},
        {"shapeID": "@a", "propertyID": "dct:date", "value_node_type": "String"},
        {"shapeID": "@b", "propertyID": "foaf:name", "value_node_type": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", propertyID="dct:creator", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:subject", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:date", value_node_type="String"
        ),
        Statement(
            start=False, shapeID="@b", propertyID="foaf:name", value_node_type="String"
        ),
    ]


def test_liststatements_without_shapeIDs():
    """Not shape IDs specified, so shape is '@default'."""
    csvrows_list = [
        {"propertyID": "dct:creator", "value_node_type": "URI"},
        {"propertyID": "dct:subject", "value_node_type": "URI"},
        {"propertyID": "dct:date", "value_node_type": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:creator",
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:subject",
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:date",
            value_node_type="String",
        ),
    ]


def test_liststatements_with_shapeIDs_specified_as_none():
    """Shape IDs specified as 'None', so shape is '@default'.
    When "shapeID" specified as 'None', row["shapeID"] will be False.
    General case: when field specified as None."""
    csvrows_list = [
        {"shapeID": None, "propertyID": "dct:creator", "value_node_type": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "value_node_type": "URI"},
        {"shapeID": None, "propertyID": "dct:date", "value_node_type": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:creator",
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:subject",
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:date",
            value_node_type="String",
        ),
    ]


def test_liststatements_with_shape_in_first_statement_only():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    csvrows_list = [
        {"shapeID": "@a", "propertyID": "dct:creator", "value_node_type": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "value_node_type": "URI"},
        {"shapeID": None, "propertyID": "dct:date", "value_node_type": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", propertyID="dct:creator", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:subject", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:date", value_node_type="String"
        ),
    ]


def test_liststatements_with_shape_on_its_own_line():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    csvrows_list = [
        {"shapeID": "@a", "propertyID": None, "value_node_type": None},
        {"shapeID": None, "propertyID": "dct:creator", "value_node_type": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "value_node_type": "URI"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", propertyID="dct:creator", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:subject", value_node_type="URI"
        ),
    ]


def test_liststatements_with_shape_on_its_own_line_fields_with_none_are_implicit():
    """Fields with value None (here: 'note' and 'start') are simply implicit."""
    csvrows_list = [
        {"shapeID": "@a", "propertyID": None, "value_node_type": None},
        {"shapeID": None, "propertyID": "dct:creator", "value_node_type": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "value_node_type": "URI"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True,
            shapeID="@a",
            propertyID="dct:creator",
            note=None,
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@a",
            propertyID="dct:subject",
            prop_label=None,
            value_node_type="URI",
        ),
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", propertyID="dct:creator", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:subject", value_node_type="URI"
        ),
    ]


def test_liststatements_with_missing_value_node_type():
    """Should parse even if input lacks field 'value_node_type'."""
    as_input = [
        {
            "shapeID": "@book",
            "propertyID": "",
            "prop_label": "Book",
            "value_constraint": "",
            "note": "",
        },
        {
            "shapeID": "",
            "propertyID": "rdf:type",
            "prop_label": "instance of",
            "value_constraint": "sdo:Book",
            "note": "must be schema.org/Book",
        },
        {
            "shapeID": "",
            "propertyID": "rdf:type",
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
            propertyID="rdf:type",
            prop_label="instance of",
            mandatory=False,
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
            propertyID="rdf:type",
            prop_label="instance of",
            mandatory=False,
            repeat=False,
            value_node_type=None,
            value_constraint="wd:Q571",
            value_constraint_type=None,
            value_shape=None,
            note="must be wikidata Book",
        ),
    ]
    assert list_statements(as_input) == expected
