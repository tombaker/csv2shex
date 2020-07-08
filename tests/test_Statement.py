"""@@@Docstring"""


import pytest
from csv2shex.csvparser import Statement


def test_statement_initialized_from_positional_arguments():
    """Statement instance initialized from positional arguments."""
    assert Statement("@photo", "dcterms:creator", "URI") == Statement(
        shape_id="@photo", prop_id="dcterms:creator", value_type="URI"
    )


def test_statement_initialized_from_positional_arguments_but_order_is_insignficant():
    """Order of arguments is insignificant (just a reminder to self)."""
    assert Statement(
        shape_id="@photo", prop_id="dcterms:creator", value_type="URI"
    ) == Statement(prop_id="dcterms:creator", shape_id="@photo", value_type="URI")


def test_statement_attributes_individually_addressable():
    """Statement instance attributes individually addressable."""
    x = Statement("@photo", "dcterms:creator", "URI")
    assert x.shape_id == "@photo"
    assert x.prop_id == "dcterms:creator"
    assert x.value_type == "URI"


def test_statement_initialized_by_assignment():
    """Statement attributes created by assignment."""
    x = Statement()
    x.shape_id = "@photo"
    x.prop_id = "dcterms:creator"
    x.value_type = "URI"
    assert x == Statement(
        shape_id="@photo", prop_id="dcterms:creator", value_type="URI"
    )


def test_statement_initialized_by_assignment_with_some_None():
    """Statement attributes created by assignment."""
    x = Statement()
    x.prop_id = "dcterms:creator"
    x.value_type = "URI"
    assert x == Statement(shape_id=None, prop_id="dcterms:creator", value_type="URI")


def test_statement_bad_attribute_initialized_by_assignment():
    """Attempted assignment to bad attribute raises TypeError."""
    x = Statement()
    x.foobar = "@photo"
    x.prop_id = "dcterms:creator"
    x.value_type = "URI"
    with pytest.raises(TypeError):
        assert x == Statement(
            foobar="@photo", prop_id="dcterms:creator", value_type="URI"
        )


