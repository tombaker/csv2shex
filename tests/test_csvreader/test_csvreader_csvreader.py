"""Read CSV file and return list of rows as Python dictionaries."""

import os
import pytest
from pathlib import Path
from csv2shex.csvreader import csvreader


def test_csvreader_with_simple_csvfile(tmp_path):
    """Simple CSV with three columns."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,propertyID,valueNodeType\n"
            ":a,dct:creator,URI\n"
            ":a,dct:subject,URI\n"
            ":a,dct:date,String\n"
        )
    )
    expected_output = [
        {"shapeID": ":a", "propertyID": "dct:creator", "valueNodeType": "URI"},
        {"shapeID": ":a", "propertyID": "dct:subject", "valueNodeType": "URI"},
        {"shapeID": ":a", "propertyID": "dct:date", "valueNodeType": "String"},
    ]
    assert csvreader(csvfile_name) == expected_output


def test_csvreader_with_complete_csvfile(tmp_path):
    """Simple CSV with all columns."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,shapeLabel,propertyID"
            ",propertyLabel,mandatory,repeatable,valueNodeType,"
            "valueDataType,valueConstraint,valueConstraintType,valueShape,note\n"
            "@a,Book,dct:creator,Creator,Y,N,URI,,,,@b,Typically the author.\n"
            "@a,Book,dct:date,Date,Y,N,String,xsd:string,(\d+/\d+/\d+),Regex,,\n"
            "@b,Person,foaf:name,Name,Y,N,String,xsd:string,,,,\n"
        )
    )
    expected_output = [
        {
            "shapeID": "@a",
            "shapeLabel": "Book",
            "propertyID": "dct:creator",
            "propertyLabel": "Creator",
            "mandatory": "Y",
            "repeatable": "N",
            "valueNodeType": "URI",
            "valueDataType": "",
            "valueConstraint": "",
            "valueConstraintType": "",
            "valueShape": "@b",
            "note": "Typically the author.",
        },
        {
            "shapeID": "@a",
            "shapeLabel": "Book",
            "propertyID": "dct:date",
            "propertyLabel": "Date",
            "mandatory": "Y",
            "repeatable": "N",
            "valueNodeType": "String",
            "valueDataType": "xsd:string",
            "valueConstraint": "(\d+/\d+/\d+)",
            "valueConstraintType": "Regex",
            "valueShape": "",
            "note": "",
        },
        {
            "shapeID": "@b",
            "shapeLabel": "Person",
            "propertyID": "foaf:name",
            "propertyLabel": "Name",
            "mandatory": "Y",
            "repeatable": "N",
            "valueNodeType": "String",
            "valueDataType": "xsd:string",
            "valueConstraint": "",
            "valueConstraintType": "",
            "valueShape": "",
            "note": "",
        },
    ]
    assert type(csvreader(csvfile_name)) == list
    assert type(expected_output) == list
    assert len(csvreader(csvfile_name)) == 3
    assert len(expected_output) == 3
    assert type(csvreader(csvfile_name)[0]) == dict
    assert csvreader(csvfile_name) == expected_output


def test_csvreader_with_invalid_csvfile(tmp_path):
    """A DCAP CSV is invalid if it does not at least have "propertyID"."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,propID,valueNodeType\n"
            ":a,dct:creator,URI\n"
        )
    )
    with pytest.raises(SystemExit):
        csvreader(csvfile_name)

