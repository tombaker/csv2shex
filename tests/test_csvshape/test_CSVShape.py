"""CSVShape object holds statements sharing a common shapeID."""

import pytest
# from csv2shex.csvshape import CSVShape

CSVSHAPE_DICT = {
    "start": True,
    "shapeID": ":a",
    "pvdicts_list": [
        {"propertyID": "dct:creator", "valueNodeType": "URI"},
        {"propertyID": "dct:subject", "valueNodeType": "URI"},
        {"propertyID": "dct:date", "valueNodeType": "String"},
    ],
}


def test_shape_fields_are_individually_addressable():
    """Fields of CSVShape instance are individually addressable."""
    shap = CSVSHAPE_DICT
    assert shap["start"]
    assert shap["shapeID"] == ":a"
    assert shap["pvdicts_list"][1] == {"propertyID": "dct:subject", "valueNodeType": "URI"}
    assert len(shap["pvdicts_list"]) == 3


def test_pvdicts_list_items_are_individually_addressable():
    """Items in pvdicts_list field of CSVShape instance are individually addressable."""
    shap = CSVSHAPE_DICT
    assert shap["pvdicts_list"][1]["propertyID"] == "dct:subject"
    assert shap["pvdicts_list"][2]["valueNodeType"] == "String"


def test_shape_initialized_by_assignment():
    """CSVShape instances can be created by assignment."""
    shap = dict()
    shap["start"] = True
    shap["shapeID"] = ":a"
    shap["pvdicts_list"] = []
    shap["pvdicts_list"].append({"propertyID": "dct:creator", "valueNodeType": "URI"})
    shap["pvdicts_list"].append({"propertyID": "dct:subject", "valueNodeType": "URI"})
    shap["pvdicts_list"].append({"propertyID": "dct:date", "valueNodeType": "String"})
    assert shap == CSVSHAPE_DICT


def test_shape_initialized_with_no_propertyvalues_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = dict()
    shap["start"] = True
    shap["shapeID"] = ":a"
    assert shap == {"start": True, "shapeID": ":a"}


def test_shape_initialized_with_no_start_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = dict()
    shap["shapeID"] = ":a"
    shap["pvdicts_list"] = []
    shap["pvdicts_list"].append({"propertyID": "dct:creator", "valueNodeType": "URI"})
    shap["pvdicts_list"].append({"propertyID": "dct:subject", "valueNodeType": "URI"})
    shap["pvdicts_list"].append({"propertyID": "dct:date", "valueNodeType": "String"})
    assert shap == {
        "shapeID": ":a",
        "pvdicts_list": [
            {"propertyID": "dct:creator", "valueNodeType": "URI"},
            {"propertyID": "dct:subject", "valueNodeType": "URI"},
            {"propertyID": "dct:date", "valueNodeType": "String"},
        ],
    }


def test_shape_initialized_with_no_shapeid_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = dict()
    shap["start"] = True
    shap["pvdicts_list"] = []
    shap["pvdicts_list"].append({"propertyID": "dct:creator", "valueNodeType": "URI"})
    shap["pvdicts_list"].append({"propertyID": "dct:subject", "valueNodeType": "URI"})
    shap["pvdicts_list"].append({"propertyID": "dct:date", "valueNodeType": "String"})
    assert shap == {
        "start": True,
        "pvdicts_list": [
            {"propertyID": "dct:creator", "valueNodeType": "URI"},
            {"propertyID": "dct:subject", "valueNodeType": "URI"},
            {"propertyID": "dct:date", "valueNodeType": "String"},
        ],
    }
