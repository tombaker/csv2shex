"""@@@Docstring"""


import pytest
from csv2shex.csv2stats import Statement


def test_statement_initialized_with_just_one_field():
    """Statement instance initialized with just one field."""
    x = Statement(prop_id="dcterms:creator")
    assert x.start == False
    assert x.shape_id == None
    assert x.prop_id == "dcterms:creator"
    assert x.v_type == None
    assert x.shape_ref == None
#    assert x.value_constraint == None
#    assert x.value_constraint_type == None
#    assert x.annot == None

def test_statement_initialized_from_positional_arguments():
    """Just a reminder that order is significant - but do not do this!"""
    assert Statement(False, "@photo", "dcterms:creator", "URI") == Statement(
        shape_id="@photo", prop_id="dcterms:creator", v_type="URI"
    )


def test_statement_initialized_from_positional_arguments_but_order_is_insignficant():
    """Order of arguments is insignificant (just a reminder to self)."""
    assert Statement(
        shape_id="@photo", prop_id="dcterms:creator", v_type="URI"
    ) == Statement(prop_id="dcterms:creator", shape_id="@photo", v_type="URI")


def test_statement_attributes_individually_addressable():
    """Statement instance attributes individually addressable."""
    x = Statement(False, "@photo", "dcterms:creator", "URI")
    assert x.shape_id == "@photo"
    assert x.prop_id == "dcterms:creator"
    assert x.v_type == "URI"


def test_statement_initialized_by_assignment():
    """Statement attributes created by assignment."""
    x = Statement()
    x.shape_id = "@photo"
    x.prop_id = "dcterms:creator"
    x.v_type = "URI"
    assert x == Statement(
        shape_id="@photo", prop_id="dcterms:creator", v_type="URI"
    )


def test_statement_initialized_by_assignment_with_some_None():
    """Statement attributes created by assignment."""
    x = Statement()
    x.prop_id = "dcterms:creator"
    x.v_type = "URI"
    assert x == Statement(shape_id=None, prop_id="dcterms:creator", v_type="URI")


def test_statement_bad_attribute_initialized_by_assignment():
    """Attempted assignment to bad attribute raises TypeError."""
    x = Statement()
    x.foobar = "@photo"
    x.prop_id = "dcterms:creator"
    x.v_type = "URI"
    with pytest.raises(TypeError):
        assert x == Statement(
            foobar="@photo", prop_id="dcterms:creator", v_type="URI"
        )
