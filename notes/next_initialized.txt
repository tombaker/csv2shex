"""Initialize instances of CSVRow."""


import pytest
from csv2shex.csvrow import CSVRow


def test_statement_initialized_with_just_one_field():
    """CSVRow instance initialized with just one field."""
    shap = CSVRow(propertyID="dcterms:creator")
    shap.normalize()
    shap.validate()
    assert shap.shapeID is None
    assert shap.shapeLabel is None
    assert shap.propertyID == "dcterms:creator"
    assert shap.propertyLabel is None
    assert shap.mandatory is False
    assert shap.repeatable is False
    assert shap.valueNodeType is None
    assert shap.valueDataType is None
    assert shap.valueConstraint is None
    assert shap.valueConstraintType is None
    assert shap.valueShape is None
    assert shap.note is None


def test_statement_initialized_without_propid():
    """CSVRow instance initialized without property ID. Shouldn't this fail?"""
    shap = CSVRow()
    assert shap.shapeID is None
    assert shap.shapeLabel is None
    assert shap.propertyID is None
    assert shap.propertyLabel is None
    assert shap.mandatory is False
    assert shap.repeatable is False
    assert shap.valueNodeType is None
    assert shap.valueDataType is None
    assert shap.valueConstraint is None
    assert shap.valueConstraintType is None
    assert shap.valueShape is None
    assert shap.note is None


def test_statement_initialized_from_named_arguments_and_order_is_insignficant():
    """Order of arguments is insignificant (just a reminder to self)."""
    assert CSVRow(
        shapeID="@photo", propertyID="dcterms:creator", valueNodeType="URI"
    ) == CSVRow(propertyID="dcterms:creator", shapeID="@photo", valueNodeType="URI")


def test_statement_fields_individually_addressable():
    """CSVRow instance fields individually addressable."""
    shap = CSVRow(shapeID="@photo", propertyID="dcterms:creator", valueNodeType="URI")
    shap.normalize()
    shap.validate()
    assert shap.shapeID == "@photo"
    assert shap.propertyID == "dcterms:creator"
    assert shap.valueNodeType == "URI"
    assert shap.valueDataType is None


def test_statement_initialized_by_assignment():
    """CSVRow instance fields created by assignment."""
    shap = CSVRow(shapeID="@photo", propertyID="dcterms:creator", valueNodeType="URI")
    shap2 = CSVRow()
    shap2.shapeID = "@photo"
    shap2.propertyID = "dcterms:creator"
    shap2.valueNodeType = "URI"
    assert shap == shap2


def test_statement_initialized_by_assignment_with_some_none():
    """CSVRow instance fields created by assignment, others have default None."""
    shap = CSVRow()
    shap.propertyID = "dcterms:creator"
    shap.valueNodeType = "URI"
    assert shap.valueDataType is None
    assert shap == CSVRow(
        shapeID=None, propertyID="dcterms:creator", valueNodeType="URI"
    )
    assert not shap.shapeID
    assert not shap.mandatory


def test_statement_bad_field_initialized_by_assignment():
    """Attempted assignment to bad field raises TypeError."""
    shap = CSVRow()
    shap.foobar = "@photo"
    shap.propertyID = "dcterms:creator"
    shap.valueNodeType = "URI"
    assert shap.valueDataType is None
    with pytest.raises(TypeError):
        assert shap == CSVRow(
            foobar="@photo", propertyID="dcterms:creator", valueNodeType="URI"
        )
