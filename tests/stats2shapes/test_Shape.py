"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.stats2shapes import list_shapes, Shape
from dataclasses import asdict

SHAPE_OBJECT = Shape(shapeid="@a", is_start_shape=True, property_values=[
            {
                "prop_id": "dct:creator",
                "v_type": "URI",
            },
            {
                "prop_id": "dct:subject",
                "v_type": "URI",
            },
            {
                "prop_id": "dct:date",
                "v_type": "String",
            }, 
    ])

LIST_OF_SHAPE_OBJECTS = [
    Shape(shapeid="@a", is_start_shape=True, property_values=[
            {
                "prop_id": "dct:creator",
                "v_type": "URI",
            },
            {
                "prop_id": "dct:subject",
                "v_type": "URI",
            },
            {
                "prop_id": "dct:date",
                "v_type": "String",
            }, 
    ]),
    Shape(shapeid="@b", is_start_shape=False, property_values=[
            {
                "prop_id": "foaf:name",
                "v_type": "String",
            },
    ])
]

# def test_shape_initialized_from_positional_arguments():
#     """Shape instance initialized from positional arguments."""
#     assert Shape("@photo", True) is False
# 
# 
# def test_statement_initialized_from_positional_arguments_but_order_is_insignficant():
#     """Order of arguments is insignificant (just a reminder to self)."""
#     assert Statement(
#         shapeid="@photo", prop_id="dcterms:creator", v_type="URI"
#     ) == Statement(prop_id="dcterms:creator", shapeid="@photo", v_type="URI")


# def test_statement_attributes_individually_addressable():
#     """Statement instance attributes individually addressable."""
#     x = Statement(False, "@photo", "dcterms:creator", "URI")
#     assert x.shapeid == "@photo"
#     assert x.prop_id == "dcterms:creator"
#     assert x.v_type == "URI"
# 
# 
# def test_statement_initialized_by_assignment():
#     """Statement attributes created by assignment."""
#     x = Statement()
#     x.shapeid = "@photo"
#     x.prop_id = "dcterms:creator"
#     x.v_type = "URI"
#     assert x == Statement(
#         shapeid="@photo", prop_id="dcterms:creator", v_type="URI"
#     )
# 
# 
# def test_statement_initialized_by_assignment_with_some_None():
#     """Statement attributes created by assignment."""
#     x = Statement()
#     x.prop_id = "dcterms:creator"
#     x.v_type = "URI"
#     assert x == Statement(shapeid=None, prop_id="dcterms:creator", v_type="URI")
# 
# 
# def test_statement_bad_attribute_initialized_by_assignment():
#     """Attempted assignment to bad attribute raises TypeError."""
#     x = Statement()
#     x.foobar = "@photo"
#     x.prop_id = "dcterms:creator"
#     x.v_type = "URI"
#     with pytest.raises(TypeError):
#         assert x == Statement(
#             foobar="@photo", prop_id="dcterms:creator", v_type="URI"
#         )
