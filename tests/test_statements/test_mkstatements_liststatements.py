"""Use list of dictionaries to initialize list of Statement objects."""

from csv2shex.mkstatements import list_statements, Statement


def test_liststatements():
    """Turn list of dictionaries into list of Statement objects."""
    csvrows_list = [
        {"shapeID": "@a", "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": "@a", "propertyID": "dct:subject", "valueNodeType": "URI"},
        {"shapeID": "@a", "propertyID": "dct:date", "valueNodeType": "String"},
        {"shapeID": "@b", "propertyID": "foaf:name", "valueNodeType": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", propertyID="dct:creator", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:subject", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:date", valueNodeType="String"
        ),
        Statement(
            start=False, shapeID="@b", propertyID="foaf:name", valueNodeType="String"
        ),
    ]


def test_liststatements_without_shapeIDs():
    """Not shape IDs specified, so shape is '@default'."""
    csvrows_list = [
        {"propertyID": "dct:creator", "valueNodeType": "URI"},
        {"propertyID": "dct:subject", "valueNodeType": "URI"},
        {"propertyID": "dct:date", "valueNodeType": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:creator",
            valueNodeType="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:subject",
            valueNodeType="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:date",
            valueNodeType="String",
        ),
    ]


def test_liststatements_with_shapeIDs_specified_as_none():
    """Shape IDs specified as 'None', so shape is '@default'.
    When "shapeID" specified as 'None', row["shapeID"] will be False.
    General case: when field specified as None."""
    csvrows_list = [
        {"shapeID": None, "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:date", "valueNodeType": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:creator",
            valueNodeType="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:subject",
            valueNodeType="URI",
        ),
        Statement(
            start=True,
            shapeID="@default",
            propertyID="dct:date",
            valueNodeType="String",
        ),
    ]


def test_liststatements_with_shape_in_first_statement_only():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    csvrows_list = [
        {"shapeID": "@a", "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:date", "valueNodeType": "String"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", propertyID="dct:creator", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:subject", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:date", valueNodeType="String"
        ),
    ]


def test_liststatements_with_shape_on_its_own_line():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    csvrows_list = [
        {"shapeID": "@a", "propertyID": None, "valueNodeType": None},
        {"shapeID": None, "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "valueNodeType": "URI"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", propertyID="dct:creator", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:subject", valueNodeType="URI"
        ),
    ]


def test_liststatements_with_shape_on_its_own_line_fields_with_none_are_implicit():
    """Fields with value None (here: 'note' and 'start') are simply implicit."""
    csvrows_list = [
        {"shapeID": "@a", "propertyID": None, "valueNodeType": None},
        {"shapeID": None, "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "valueNodeType": "URI"},
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True,
            shapeID="@a",
            propertyID="dct:creator",
            note=None,
            valueNodeType="URI",
        ),
        Statement(
            start=True,
            shapeID="@a",
            propertyID="dct:subject",
            propertyLabel=None,
            valueNodeType="URI",
        ),
    ]
    assert list_statements(csvrows_list) == [
        Statement(
            start=True, shapeID="@a", propertyID="dct:creator", valueNodeType="URI"
        ),
        Statement(
            start=True, shapeID="@a", propertyID="dct:subject", valueNodeType="URI"
        ),
    ]


def test_liststatements_with_missing_valueNodeType():
    """Should parse even if input lacks field 'valueNodeType'."""
    as_input = [
        {
            "shapeID": "@book",
            "propertyID": "",
            "propertyLabel": "Book",
            "value_constraint": "",
            "note": "",
        },
        {
            "shapeID": "",
            "propertyID": "rdf:type",
            "propertyLabel": "instance of",
            "value_constraint": "sdo:Book",
            "note": "must be schema.org/Book",
        },
        {
            "shapeID": "",
            "propertyID": "rdf:type",
            "propertyLabel": "instance of",
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
            propertyLabel="instance of",
            mandatory=False,
            repeatable=False,
            valueNodeType=None,
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
            propertyLabel="instance of",
            mandatory=False,
            repeatable=False,
            valueNodeType=None,
            value_constraint="wd:Q571",
            value_constraint_type=None,
            value_shape=None,
            note="must be wikidata Book",
        ),
    ]
    assert list_statements(as_input) == expected
