"""Shape object holds statements sharing a common shape_id."""

import os
import pytest
from pathlib import Path
from csv2shex.stats2shapes import list_shapes, Shape
from dataclasses import asdict

SHAPE_OBJECT = Shape(
    start=True,
    shape_id="@a",
    property_values=[
        {"prop_id": "dct:creator", "value_type": "URI"},
        {"prop_id": "dct:subject", "value_type": "URI"},
        {"prop_id": "dct:date", "value_type": "String"},
    ],
)


def test_shape_fields_individually_addressable():
    """Shape fields individually addressable."""
    x = SHAPE_OBJECT
    assert x.start
    assert x.shape_id == "@a"
    assert x.property_values[1] == {"prop_id": "dct:subject", "value_type": "URI"}


def test_shape_initialized_by_assignment():
    """Shape fields created by assignment."""
    x = Shape()
    x.start = True
    x.shape_id = "@a"
    x.property_values = []
    x.property_values.append({"prop_id": "dct:creator", "value_type": "URI"})
    x.property_values.append({"prop_id": "dct:subject", "value_type": "URI"})
    x.property_values.append({"prop_id": "dct:date", "value_type": "String"})
    assert x == SHAPE_OBJECT


def test_shape_initialized_with_no_propertyvalues_field_should_pass_FOR_NOW():
    """Test should pass for now but this condition should raise exception."""
    x = Shape()
    x.start = True
    x.shape_id = "@a"
    assert x == Shape(start=True, shape_id="@a")


def test_shape_initialized_with_no_start_field_should_pass_FOR_NOW():
    """Test should pass for now but this condition should raise exception."""
    x = Shape()
    x.shape_id = "@a"
    x.property_values = []
    x.property_values.append({"prop_id": "dct:creator", "value_type": "URI"})
    x.property_values.append({"prop_id": "dct:subject", "value_type": "URI"})
    x.property_values.append({"prop_id": "dct:date", "value_type": "String"})
    assert x == Shape(
        shape_id="@a",
        property_values=[
            {"prop_id": "dct:creator", "value_type": "URI"},
            {"prop_id": "dct:subject", "value_type": "URI"},
            {"prop_id": "dct:date", "value_type": "String"},
        ],
    )

def test_shape_initialized_with_no_shapeid_field_should_pass_FOR_NOW():
    """Test should pass for now but this condition should raise exception."""
    x = Shape()
    x.start = True
    x.property_values = []
    x.property_values.append({"prop_id": "dct:creator", "value_type": "URI"})
    x.property_values.append({"prop_id": "dct:subject", "value_type": "URI"})
    x.property_values.append({"prop_id": "dct:date", "value_type": "String"})
    assert x == Shape(
        start=True,
        property_values=[
            {"prop_id": "dct:creator", "value_type": "URI"},
            {"prop_id": "dct:subject", "value_type": "URI"},
            {"prop_id": "dct:date", "value_type": "String"},
        ],
    )
