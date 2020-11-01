"""Pretty-print CSVShape objects to console."""

import pytest
from textwrap import dedent
from csv2shex.csvshapes import pprint_shapes, list_csvshapes, CSVShape
from csv2shex.csvrows import CSVRow


def test_list_csvshapes_two_shapes():
    """Turn list of CSVRow objects into list with two CSVShapes."""
    csvshapes_list = [
        CSVShape(
            start=True,
            shapeID=":a",
            shapeLabel=None,
            shapeClosed=False,
            statement_csvrows_list=[
                {
                    "propertyID": "dct:creator",
                    "mandatory": False,
                    "note": None,
                    "propertyLabel": None,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueDataType": None,
                    "valueNodeType": None,
                    "valueShape": None,
                },
                {
                    "propertyID": "dct:date",
                    "mandatory": False,
                    "note": None,
                    "propertyLabel": None,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueDataType": None,
                    "valueNodeType": None,
                    "valueShape": None,
                },
            ],
        ),
        CSVShape(
            start=False,
            shapeID=":b",
            shapeLabel=None,
            statement_csvrows_list=[
                {
                    "propertyID": "foaf:name",
                    "mandatory": False,
                    "note": None,
                    "propertyLabel": None,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueDataType": None,
                    "valueNodeType": None,
                    "valueShape": None,
                }
            ],
        ),
    ]
    expected_output_indented = """\
    DCAP
        Shape
            shapeID: :a
            start: True
            Statement
                propertyID: dct:creator
            Statement
                propertyID: dct:date
        Shape
            shapeID: :b
            Statement
                propertyID: foaf:name
    """
    #print("")
    #print(pprint_shapes(csvshapes_list))
    #print("")
    #print(dedent(expected_output_indented))
    assert pprint_shapes(csvshapes_list) == dedent(expected_output_indented).splitlines()

