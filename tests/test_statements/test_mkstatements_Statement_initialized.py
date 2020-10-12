"""Initialize instances of Statement."""


import pytest
from csv2shex.mkstatements import Statement


def test_statement_initialized_with_just_one_field():
    """Statement instance initialized with just one field."""
    shap = Statement(propertyID="dcterms:creator")
    assert not shap.start
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
    """Statement instance initialized without property ID. Shouldn't this fail?"""
    shap = Statement()
    assert not shap.start
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
    assert Statement(
        shapeID="@photo", propertyID="dcterms:creator", valueNodeType="URI"
    ) == Statement(
        propertyID="dcterms:creator", shapeID="@photo", valueNodeType="URI"
    )


def test_statement_fields_individually_addressable():
    """Statement instance fields individually addressable."""
    shap = Statement(
        shapeID="@photo", propertyID="dcterms:creator", valueNodeType="URI"
    )
    assert shap.shapeID == "@photo"
    assert shap.propertyID == "dcterms:creator"
    assert shap.valueNodeType == "URI"
    assert shap.valueDataType is None


def test_statement_initialized_by_assignment():
    """Statement instance fields created by assignment."""
    shap = Statement(
        shapeID="@photo", propertyID="dcterms:creator", valueNodeType="URI"
    )
    shap2 = Statement()
    shap2.shapeID = "@photo"
    shap2.propertyID = "dcterms:creator"
    shap2.valueNodeType = "URI"
    assert shap == shap2


def test_statement_initialized_by_assignment_with_some_none():
    """Statement instance fields created by assignment, others have default None."""
    shap = Statement()
    shap.propertyID = "dcterms:creator"
    shap.valueNodeType = "URI"
    assert shap.valueDataType is None
    assert shap == Statement(
        shapeID=None, propertyID="dcterms:creator", valueNodeType="URI"
    )
    assert not shap.shapeID
    assert not shap.mandatory


def test_statement_bad_field_initialized_by_assignment():
    """Attempted assignment to bad field raises TypeError."""
    shap = Statement()
    shap.foobar = "@photo"
    shap.propertyID = "dcterms:creator"
    shap.valueNodeType = "URI"
    assert shap.valueDataType is None
    with pytest.raises(TypeError):
        assert shap == Statement(
            foobar="@photo", propertyID="dcterms:creator", valueNodeType="URI"
        )
