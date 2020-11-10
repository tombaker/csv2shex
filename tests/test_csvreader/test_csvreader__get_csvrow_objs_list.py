"""Use list of dictionaries to initialize list of CSVRow objects."""

from csv2shex.csvrow import CSVRow
from csv2shex.csvreader import _get_csvrow_objs_list


def test_liststatements():
    """Turn list of dictionaries into list of CSVRow objects."""
    csvrows_list = [
        {"shapeID": ":a", "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": ":a", "propertyID": "dct:subject", "valueNodeType": "URI"},
        {"shapeID": ":a", "propertyID": "dct:date", "valueNodeType": "String"},
        {"shapeID": ":b", "propertyID": "foaf:name", "valueNodeType": "String"},
    ]
    assert _get_csvrow_objs_list(csvrows_list) == [
        CSVRow(shapeID=":a", propertyID="dct:creator", valueNodeType="URI"),
        CSVRow(shapeID=":a", propertyID="dct:subject", valueNodeType="URI"),
        CSVRow(shapeID=":a", propertyID="dct:date", valueNodeType="String"),
        CSVRow(shapeID=":b", propertyID="foaf:name", valueNodeType="String"),
    ]


def test_liststatements_without_shapeIDs():
    """Not shape IDs specified, so shape is ':default'."""
    csvrows_list = [
        {"propertyID": "dct:creator", "valueNodeType": "URI"},
        {"propertyID": "dct:subject", "valueNodeType": "URI"},
        {"propertyID": "dct:date", "valueNodeType": "String"},
    ]
    assert _get_csvrow_objs_list(csvrows_list) == [
        CSVRow(
            shapeID=":default",
            propertyID="dct:creator",
            valueNodeType="URI",
        ),
        CSVRow(
            shapeID=":default",
            propertyID="dct:subject",
            valueNodeType="URI",
        ),
        CSVRow(
            shapeID=":default",
            propertyID="dct:date",
            valueNodeType="String",
        ),
    ]


def test_liststatements_with_shapeIDs_specified_as_none():
    """Shape IDs specified as 'None', so shape is ':default'.
    When "shapeID" specified as 'None', row["shapeID"] will be False.
    General case: when field specified as None."""
    csvrows_list = [
        {"shapeID": None, "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:date", "valueNodeType": "String"},
    ]
    assert _get_csvrow_objs_list(csvrows_list) == [
        CSVRow(
            shapeID=":default",
            propertyID="dct:creator",
            valueNodeType="URI",
        ),
        CSVRow(
            shapeID=":default",
            propertyID="dct:subject",
            valueNodeType="URI",
        ),
        CSVRow(
            shapeID=":default",
            propertyID="dct:date",
            valueNodeType="String",
        ),
    ]


def test_liststatements_with_shape_in_first_statement_only():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    csvrows_list = [
        {"shapeID": ":a", "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:date", "valueNodeType": "String"},
    ]
    assert _get_csvrow_objs_list(csvrows_list) == [
        CSVRow(shapeID=":a", propertyID="dct:creator", valueNodeType="URI"),
        CSVRow(shapeID=":a", propertyID="dct:subject", valueNodeType="URI"),
        CSVRow(shapeID=":a", propertyID="dct:date", valueNodeType="String"),
    ]


def test_liststatements_with_shape_on_its_own_line():
    """If shape IDs used previously, used for subsequent statements if no Shape ID."""
    csvrows_list = [
        {"shapeID": ":a", "propertyID": None, "valueNodeType": None},
        {"shapeID": None, "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "valueNodeType": "URI"},
    ]
    assert _get_csvrow_objs_list(csvrows_list) == [
        CSVRow(shapeID=":a", propertyID="dct:creator", valueNodeType="URI"),
        CSVRow(shapeID=":a", propertyID="dct:subject", valueNodeType="URI"),
    ]


def test_liststatements_with_shape_on_its_own_line_fields_with_none_are_implicit():
    """Fields with value None (here: 'note' and 'start') are simply implicit."""
    csvrows_list = [
        {"shapeID": ":a", "propertyID": None, "valueNodeType": None},
        {"shapeID": None, "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": None, "propertyID": "dct:subject", "valueNodeType": "URI"},
    ]
    assert _get_csvrow_objs_list(csvrows_list) == [
        CSVRow(
            shapeID=":a",
            propertyID="dct:creator",
            note=None,
            valueNodeType="URI",
        ),
        CSVRow(
            shapeID=":a",
            propertyID="dct:subject",
            propertyLabel=None,
            valueNodeType="URI",
        ),
    ]
    assert _get_csvrow_objs_list(csvrows_list) == [
        CSVRow(shapeID=":a", propertyID="dct:creator", valueNodeType="URI"),
        CSVRow(shapeID=":a", propertyID="dct:subject", valueNodeType="URI"),
    ]


def test_liststatements_with_missing_valueNodeType():
    """Should parse even if input lacks field 'valueNodeType'."""
    as_input = [
        {
            "shapeID": ":book",
            "propertyID": "",
            "propertyLabel": "Book",
            "valueConstraint": "",
            "note": "",
        },
        {
            "shapeID": "",
            "propertyID": "rdf:type",
            "propertyLabel": "instance of",
            "valueConstraint": "sdo:Book",
            "note": "must be schema.org/Book",
        },
        {
            "shapeID": "",
            "propertyID": "rdf:type",
            "propertyLabel": "instance of",
            "valueConstraint": "wd:Q571",
            "note": "must be wikidata Book",
        },
    ]
    expected = [
        CSVRow(
            shapeID=":book",
            shapeLabel=None,
            propertyID="rdf:type",
            propertyLabel="instance of",
            mandatory=None,
            repeatable=None,
            valueNodeType=None,
            valueConstraint="sdo:Book",
            valueConstraintType=None,
            valueShape=None,
            note="must be schema.org/Book",
        ),
        CSVRow(
            shapeID=":book",
            shapeLabel=None,
            propertyID="rdf:type",
            propertyLabel="instance of",
            mandatory=None,
            repeatable=None,
            valueNodeType=None,
            valueConstraint="wd:Q571",
            valueConstraintType=None,
            valueShape=None,
            note="must be wikidata Book",
        ),
    ]
    assert _get_csvrow_objs_list(as_input) == expected
