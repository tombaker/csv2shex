"""Pretty-print Shapes to console."""

from textwrap import dedent
from csv2shex.mkshapes import pprint_shapes, list_shapes, Shape
from csv2shex.mkstatements import Statement

def test_pprint_shapes():
    """@@@Docstring"""
    as_input = [
        Shape(
            start=True,
            shape_id="@a",
            shape_label=None,
            shape_statements=[
                {
                    "prop_id": "dct:creator",
                    "value_type": "URI",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                },
                {
                    "prop_id": "dct:date",
                    "value_type": "String",
                    "prop_label": None,
                    "mand": None,
                    "repeat": None,
                    "value_datatype": None,
                    "constraint_value": None,
                    "constraint_type": None,
                    "shape_ref": None,
                    "annot": None,
                },
            ],
        )
    ]
    as_output = dedent("""\
    Shape
        start: True
        shape_id: @a
        Statement
            prop_id: dct:creator
            value_type: URI
        Statement
            prop_id: dct:date
            value_type: String
    """)
    print(pprint_shapes(as_input))
    assert pprint_shapes(as_input) == as_output


as_input = [
    Shape(
        start=True,
        shape_id="@a",
        shape_label=None,
        shape_statements=[
            {
                "prop_id": "dct:creator",
                "value_type": "URI",
                "prop_label": None,
                "mand": None,
                "repeat": None,
                "value_datatype": None,
                "constraint_value": None,
                "constraint_type": None,
                "shape_ref": None,
                "annot": None,
            },
            {
                "prop_id": "dct:date",
                "value_type": "String",
                "prop_label": None,
                "mand": None,
                "repeat": None,
                "value_datatype": None,
                "constraint_value": None,
                "constraint_type": None,
                "shape_ref": None,
                "annot": None,
            },
        ],
    )
]
