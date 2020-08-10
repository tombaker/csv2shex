"""Initialize instances of Statement."""


import pytest
from csv2shex.mkstatements import Statement


def test_statement_initialized_with_just_one_field():
    """Statement instance initialized with just one field."""
    shap = Statement(prop_id="dcterms:creator")
    assert not shap.start
    assert shap.shape_id is None
    assert shap.shape_label is None
    assert shap.prop_id == "dcterms:creator"
    assert shap.prop_label is None
    assert shap.mand is False
    assert shap.repeat is False
    assert shap.value_type is None
    assert shap.constraint_value is None
    assert shap.constraint_type is None
    assert shap.shape_ref is None
    assert shap.annot is None


def test_statement_initialized_without_propid():
    """Statement instance initialized without property ID. Shouldn't this fail?"""
    shap = Statement()
    assert not shap.start
    assert shap.shape_id is None
    assert shap.shape_label is None
    assert shap.prop_id is None
    assert shap.prop_label is None
    assert shap.mand is False
    assert shap.repeat is False
    assert shap.value_type is None
    assert shap.constraint_value is None
    assert shap.constraint_type is None
    assert shap.shape_ref is None
    assert shap.annot is None


def test_statement_initialized_from_named_arguments_and_order_is_insignficant():
    """Order of arguments is insignificant (just a reminder to self)."""
    assert Statement(
        shape_id="@photo", prop_id="dcterms:creator", value_type="URI"
    ) == Statement(prop_id="dcterms:creator", shape_id="@photo", value_type="URI")


def test_statement_fields_individually_addressable():
    """Statement instance fields individually addressable."""
    shap = Statement(shape_id="@photo", prop_id="dcterms:creator", value_type="URI")
    assert shap.shape_id == "@photo"
    assert shap.prop_id == "dcterms:creator"
    assert shap.value_type == "URI"


def test_statement_initialized_by_assignment():
    """Statement instance fields created by assignment."""
    shap = Statement(shape_id="@photo", prop_id="dcterms:creator", value_type="URI")
    shap2 = Statement()
    shap2.shape_id = "@photo"
    shap2.prop_id = "dcterms:creator"
    shap2.value_type = "URI"
    assert shap == shap2


def test_statement_initialized_by_assignment_with_some_none():
    """Statement instance fields created by assignment, others have default None."""
    shap = Statement()
    shap.prop_id = "dcterms:creator"
    shap.value_type = "URI"
    assert shap == Statement(shape_id=None, prop_id="dcterms:creator", value_type="URI")
    assert not shap.shape_id
    assert not shap.mand


def test_statement_bad_field_initialized_by_assignment():
    """Attempted assignment to bad field raises TypeError."""
    shap = Statement()
    shap.foobar = "@photo"
    shap.prop_id = "dcterms:creator"
    shap.value_type = "URI"
    with pytest.raises(TypeError):
        assert shap == Statement(
            foobar="@photo", prop_id="dcterms:creator", value_type="URI"
        )
