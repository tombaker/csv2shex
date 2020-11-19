"""Turn list of CSVRows into list of CSVShapes."""

import pytest
from pprint import pprint
from dataclasses import asdict
from csv2shex.csvshape import CSVShape
from csv2shex.csvrow import CSVRow
from csv2shex.csvshape import get_csvshape_dicts_list


def test_get_csvshape_dicts_list_one_shape():
    """Get csvshape dict with one shape from list of CSVRow object(s)."""
    csvrow_objs_list = [
        CSVRow(shapeID=":a", propertyID="dct:creator"),
    ]

    csvshape_dicts_list = get_csvshape_dicts_list(csvrow_objs_list)
    assert csvshape_dicts_list[0]["shapeID"] == ":a"
    assert csvshape_dicts_list[0]["start"]
    assert csvshape_dicts_list[0]["pvdicts_list"]
    assert csvshape_dicts_list[0]["pvdicts_list"][0]["propertyID"] == "dct:creator"
    assert not csvshape_dicts_list[0]["pvdicts_list"][0]["mandatory"]
    expected_csvshape_dicts_list = [
        {
            "shapeID": ":a",
            "shapeLabel": None,
            "start": True,
            "shapeClosed": None,
            "pvdicts_list": [
                {
                    "propertyID": "dct:creator",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": None,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
            ],
        }
    ]
    assert csvshape_dicts_list == expected_csvshape_dicts_list


def test_get_csvshape_dicts_list_two_shapes():
    """Get csvshape dict with two shapes from list of CSVRow objects."""
    csvrow_objs_list = [
        CSVRow(shapeID=":a", propertyID="dct:creator"),
        CSVRow(shapeID=":a", propertyID="dct:date"),
        CSVRow(shapeID=":b", propertyID="foaf:name"),
    ]
    csvshape_dicts_list = get_csvshape_dicts_list(csvrow_objs_list)
    assert csvshape_dicts_list[1]["shapeID"] == ":b"
    assert not csvshape_dicts_list[1]["start"]
    assert csvshape_dicts_list[1]["pvdicts_list"][0]["propertyID"] == "foaf:name"


def test_get_csvshape_dicts_list_takes_label_for_first_shapeid_encountered():
    """Csvshape dict takes shapeLabel for any new shapeID encountered."""
    csvrow_objs_list = [
        CSVRow(shapeID=":a", shapeLabel="Author", propertyID="dct:creator"),
        CSVRow(shapeID=":a", shapeLabel="Creator", propertyID="dct:date"),
    ]
    csvshape_dicts_list = get_csvshape_dicts_list(csvrow_objs_list)
    assert csvshape_dicts_list[0]["shapeLabel"] == "Author"


def test_get_csvshape_dicts_list_assigns_start_to_first_shape_created():
    """First shape created is marked as 'start' shape."""
    csvrow_objs_list = [
        CSVRow(shapeID=":a", propertyID=":propa"),
        CSVRow(shapeID=":b", propertyID=":propb"),
    ]
    csvshape_dicts_list = get_csvshape_dicts_list(csvrow_objs_list)
    assert csvshape_dicts_list[0]["start"]
    assert not csvshape_dicts_list[1]["start"]
