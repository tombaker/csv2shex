"""Turn list of Shapes into YAML string."""

from csv2shex.mkshapes import Shape
from csv2shex.mkyaml import csv2yaml


def test_csv2yaml():
    as_input = [
        Shape(
            start=True,
            shape_id="@a",
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
                    "prop_id": "dct:subject",
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
        ),
        Shape(
            start=False,
            shape_id="@b",
            shape_statements=[
                {
                    "prop_id": "foaf:name",
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
    expected = None
    assert csv2yaml(as_input) == expected
