"""Turn list of CSVRows into list of CSVShapes."""

import pytest
from pprint import pprint
from dataclasses import asdict
from csv2shex.csvrow import CSVRow
from csv2shex.csvshape import get_csvshape_dicts_list

DEFAULTS = asdict(CSVRow())


def test_get_csvshape_dicts_list_one_shape():
    """Get csvshape dict with one shape from list of csvrow dicts."""
    override_dicts_list = [{"shapeID": ":a", "propertyID": "dct:creator"}]
    full_csvrow_dicts_list = [dict(DEFAULTS, **i) for i in override_dicts_list]
    csvshape_dicts_list = get_csvshape_dicts_list(full_csvrow_dicts_list)
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
            "shapeClosed": False,
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


@pytest.mark.skip
def test_get_csvshape_dicts_list_two_shapes():
    """Get csvshape dict with two shape from list of csvrow dicts."""
    override_dicts_list = [
        {"shapeID": ":a", "propertyID": "dct:creator"},
        {"shapeID": ":b", "propertyID": "foaf:name"},
    ]
    full_csvrow_dicts_list = [dict(DEFAULTS, **i) for i in override_dicts_list]
    csvshape_dicts_list = get_csvshape_dicts_list(full_csvrow_dicts_list)
    assert csvshape_dicts_list[1]["shapeID"] == ":b"
    assert not csvshape_dicts_list[1]["start"]
    assert csvshape_dicts_list[1]["pvdicts_list"][0]["propertyID"] == "foaf:name"


@pytest.mark.skip
def test_get_csvshape_dicts_list_takes_label_for_first_shapeid_encountered():
    """Csvshape dict takes shapeLabel for any new shapeID encountered."""
    override_dicts_list = [
        {"shapeID": ":a", "shapeLabel": "Author", "propertyID": "dct:creator"},
        {"shapeID": ":a", "shapeLabel": "Creator", "propertyID": "dct:subject"},
    ]
    full_csvrow_dicts_list = [dict(DEFAULTS, **i) for i in override_dicts_list]
    csvshape_dicts_list = get_csvshape_dicts_list(full_csvrow_dicts_list)
    assert csvshape_dicts_list[0]["shapeLabel"] == "Author"


@pytest.mark.skip
def test_get_csvshape_dicts_list_assigns_start_to_first_shape_created():
    """First csvshape created is marked as 'start' shape."""
    override_dicts_list = [
        {"shapeID": ":a", "propertyID": ":propa"},
        {"shapeID": ":b", "propertyID": ":propb"},
    ]
    full_csvrow_dicts_list = [dict(DEFAULTS, **i) for i in override_dicts_list]
    csvshape_dicts_list = get_csvshape_dicts_list(full_csvrow_dicts_list)
    assert csvshape_dicts_list[0]["start"]
    assert not csvshape_dicts_list[1]["start"]
