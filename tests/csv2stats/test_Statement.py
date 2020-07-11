"""Initialize instances of Statement."""


import pytest
from csv2shex.csv2stats import Statement


def test_statement_initialized_with_just_one_field():
    """Statement instance initialized with just one field."""
    x = Statement(prop_id="dcterms:creator")
    assert x.start == False
    assert x.shape_id == None
    assert x.shape_label == None
    assert x.prop_id == "dcterms:creator"
    assert x.prop_label == None
    assert x.mand == None
    assert x.repeat == None
    assert x.value_type == None
    assert x.value_datatype == None
    assert x.constraint_value == None
    assert x.constraint_type == None
    assert x.shape_ref == None
    assert x.annot == None


def test_statement_initialized_without_property_id():
    """Statement instance initialized without property ID. Shouldn't this fail?"""
    x = Statement()
    assert x.start == False
    assert x.shape_id == None
    assert x.shape_label == None
    assert x.prop_id == None
    assert x.prop_label == None
    assert x.mand == None
    assert x.repeat == None
    assert x.value_type == None
    assert x.value_datatype == None
    assert x.constraint_value == None
    assert x.constraint_type == None
    assert x.shape_ref == None
    assert x.annot == None


def test_statement_initialized_from_named_arguments_and_order_is_insignficant():
    """Order of arguments is insignificant (just a reminder to self)."""
    assert Statement(
        shape_id="@photo", prop_id="dcterms:creator", value_type="URI"
    ) == Statement(prop_id="dcterms:creator", shape_id="@photo", value_type="URI")


def test_statement_fields_individually_addressable():
    """Statement instance fields individually addressable."""
    x = Statement(shape_id="@photo", prop_id="dcterms:creator", value_type="URI")
    assert x.shape_id == "@photo"
    assert x.prop_id == "dcterms:creator"
    assert x.value_type == "URI"


def test_statement_initialized_by_assignment():
    """Statement instance fields created by assignment."""
    x = Statement(shape_id="@photo", prop_id="dcterms:creator", value_type="URI")
    y = Statement()
    y.shape_id = "@photo"
    y.prop_id = "dcterms:creator"
    y.value_type = "URI"
    assert x == y


def test_statement_initialized_by_assignment_with_some_None():
    """Statement instance fields created by assignment, others have default None."""
    x = Statement()
    x.prop_id = "dcterms:creator"
    x.value_type = "URI"
    assert x == Statement(shape_id=None, prop_id="dcterms:creator", value_type="URI")
    assert not x.shape_id
    assert not x.mand


def test_statement_bad_field_initialized_by_assignment():
    """Attempted assignment to bad field raises TypeError."""
    x = Statement()
    x.foobar = "@photo"
    x.prop_id = "dcterms:creator"
    x.value_type = "URI"
    with pytest.raises(TypeError):
        assert x == Statement(
            foobar="@photo", prop_id="dcterms:creator", value_type="URI"
        )
