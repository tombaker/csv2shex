"""Read CSV file and return list of rows as Python dictionaries."""

import pytest
from csv2shex.csvreader import _get_csvshapes
from csv2shex.csvshape import CSVShape, CSVTripleConstraint


def test_get_csvshapes_one_default_shape():
    """CSV: one default shape."""
    rows = [
        { "shapeID": "", "propertyID": "dc:creator", },
        { "shapeID": "", "propertyID": "dc:date", },
    ]
    expected_shapes = [
        CSVShape(
            shapeID=":default",
            start=True,
            tc_list=[
                CSVTripleConstraint(propertyID="dc:creator"),
                CSVTripleConstraint(propertyID="dc:date"),
            ],
        ),
    ]
    assert _get_csvshapes(rows) == expected_shapes


def test_get_csvshapes_twoshapes_first_is_default():
    """CSV: two shapes, first of which is default."""
    rows = [
        { "shapeID": "", "propertyID": "dc:creator", },
        { "shapeID": "", "propertyID": "dc:type", },
        { "shapeID": ":author", "propertyID": "foaf:name", },
    ]
    expected_shapes = [
        CSVShape(
            shapeID=":default",
            start=True,
            tc_list=[
                CSVTripleConstraint(propertyID="dc:creator"),
                CSVTripleConstraint(propertyID="dc:type"),
            ],
        ),
        CSVShape(
            shapeID=":author",
            start=False,
            tc_list=[
                CSVTripleConstraint(
                    propertyID="foaf:name", valueConstraint="", valueShape=""
                )
            ],
        ),
    ]
    assert _get_csvshapes(rows) == expected_shapes


def test_get_csvshapes_default_shape_because_shapeID_not_specified():
    """One shape, default, because shapeID is not specified."""
    rows = [
        { "propertyID": "dc:creator", },
    ]
    expected_shapes = [
        CSVShape(
            shapeID=":default",
            start=True,
            tc_list=[
                CSVTripleConstraint(propertyID="dc:creator"),
            ],
        ),
    ]
    assert _get_csvshapes(rows) == expected_shapes


def test_get_csvshapes_twoshapes_first_is_default_because_shapeID_empty():
    """CSV: two shapes, first of which is default because shapeID is empty."""
    rows = [
        { "shapeID": "", "propertyID": "dc:creator", },
        { "shapeID": "", "propertyID": "dc:type", },
        { "shapeID": ":author", "propertyID": "foaf:name", },
    ]
    expected_shapes = [
        CSVShape(
            shapeID=":default",
            start=True,
            tc_list=[
                CSVTripleConstraint(propertyID="dc:creator"),
                CSVTripleConstraint(propertyID="dc:type"),
            ],
        ),
        CSVShape(
            shapeID=":author",
            start=False,
            tc_list=[
                CSVTripleConstraint(
                    propertyID="foaf:name", valueConstraint="", valueShape=""
                )
            ],
        ),
    ]
    assert _get_csvshapes(rows) == expected_shapes


# passes
def test_get_csvshapes_two_shapes_one_property_each():
    """CSV: two shapes, one property each."""
    rows = [
        { "shapeID": ":book", "propertyID": "dc:creator", },
        { "shapeID": "", "propertyID": "dc:type", },
        { "shapeID": ":author", "propertyID": "foaf:name", },
    ]
    expected_shapes = [
        CSVShape(
            shapeID=":book",
            start=True,
            tc_list=[
                CSVTripleConstraint(propertyID="dc:creator"),
                CSVTripleConstraint(propertyID="dc:type"),
            ],
        ),
        CSVShape(
            shapeID=":author",
            tc_list=[CSVTripleConstraint(propertyID="foaf:name")],
        ),
    ]
    assert _get_csvshapes(rows) == expected_shapes


