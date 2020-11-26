"""Read CSV file and return list of rows as Python dictionaries."""

import os
from pathlib import Path
import pytest
from csv2shex.csvreader import _get_rows


def test_get_rows_with_invalid_csvfile(tmp_path):
    """A DCAP CSV is invalid if it does not at least have "propertyID"."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(("shapeID,propID,valueNodeType\n" ":a,dct:creator,URI\n"))
    with pytest.raises(SystemExit):
        _get_rows(csvfile_name)


def test_get_rows_with_minimal_csvfile(tmp_path):
    """Minimal CSV with three columns."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,propertyID,valueConstraint,valueShape\n"
            ":buch,dc:creator,,:autor\n"
            ",dc:type,schema:Book,\n"
            ":autor,ex:name,,\n"
        )
    )
    expected_csvrow_dicts_list = [
        {
            'shapeID': ':buch',
            'propertyID': 'dc:creator',
            'valueConstraint': '',
            'valueShape': ':autor'
        }, {
            'shapeID': '',
            'propertyID': 'dc:type',
            'valueConstraint': 'schema:Book',
            'valueShape': ''
        }, {
            'shapeID': ':autor',
            'propertyID': 'ex:name',
            'valueConstraint': '',
            'valueShape': ''
        }
    ]
    assert _get_rows(csvfile_name) == expected_csvrow_dicts_list


def test_get_rows_with_simple_csvfile(tmp_path):
    """Another simple CSV with three columns."""
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
    expected_csvrow_dicts_list = [
        {'shapeID': ':a', 'propertyID': 'dct:creator', 'valueNodeType': 'URI'},
        {'shapeID': ':a', 'propertyID': 'dct:subject', 'valueNodeType': 'URI'},
        {'shapeID': ':a', 'propertyID': 'dct:date', 'valueNodeType': 'String'}
    ]
    assert _get_rows(csvfile_name) == expected_csvrow_dicts_list


def test_get_rows_with_complete_csvfile(tmp_path):
    """Simple CSV with all columns."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,shapeLabel,propertyID"
            ",propertyLabel,mandatory,repeatable,valueNodeType,"
            "valueDataType,valueConstraint,valueConstraintType,valueShape,note\n"
            ":a,Book,dct:creator,Creator,Y,N,URI,,,,:b,Typically the author.\n"
            ":b,Person,ex:name,Name,Y,N,String,xsd:string,,,,\n"
        )
    )
    corrected_csvrows_list = [
        {
            "shapeID": ":a",
            "shapeLabel": "Book",
            "shapeClosed": False,
            "propertyID": "dct:creator",
            "propertyLabel": "Creator",
            "mandatory": True,
            "repeatable": False,
            "valueNodeType": "URI",
            "valueDataType": "",
            "valueConstraint": "",
            "valueConstraintType": "",
            "valueShape": ":b",
            "note": "Typically the author.",
        },
        {
            "shapeID": ":b",
            "shapeLabel": "Person",
            "shapeClosed": False,
            "propertyID": "ex:name",
            "propertyLabel": "Name",
            "mandatory": True,
            "repeatable": False,
            "valueNodeType": "String",
            "valueDataType": "xsd:string",
            "valueConstraint": "",
            "valueConstraintType": "",
            "valueShape": "",
            "note": "",
        },
    ]
    assert isinstance(_get_rows(csvfile_name), list)
    assert _get_rows(csvfile_name)[0]["mandatory"]
    assert isinstance(corrected_csvrows_list, list)
    assert len(_get_rows(csvfile_name)) == 2
    assert len(corrected_csvrows_list) == 2


def test_liststatements_with_csv_column_outside_dctap_model_are_ignored(tmp_path):
    """CSV columns not part of the DC TAP model are simply ignored."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,propertyID,confidential\n"
            ":a,dct:subject,True\n"
        )
    )
    expected_csvrow_dicts_list = [
        {"shapeID": ":a", "propertyID": "dct:subject", "confidential": "True"},
    ]
    assert _get_rows(csvfile_name) == expected_csvrow_dicts_list
