"""Read CSV file and return list of rows as Python dictionaries."""

import os
import pytest
from pathlib import Path
from csv2shex.csvreader import csvreader
from csv2shex.csvrow import CSVRow


@pytest.mark.csvshape
@pytest.mark.skip
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

@pytest.mark.csvshape
@pytest.mark.skip
def test_csvreader_with_complete_csvfile(tmp_path):
    """Simple CSV with all columns."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,shapeLabel,propertyID"
            ",propertyLabel,mandatory,repeatable,valueNodeType,"
            "valueDataType,valueConstraint,valueConstraintType,valueShape,note\n"
            ":a,Book,dct:creator,Creator,Y,N,URI,,,,:b,Typically the author.\n"
            ":b,Person,foaf:name,Name,Y,N,String,xsd:string,,,,\n"
        )
    )

    expected_output = [
	CSVRow(
                shapeID=':a', shapeLabel='Book', shapeClosed=None, start=None, propertyID='dct:creator', propertyLabel='Creator', mandatory=True, repeatable=False, valueNodeType='URI', valueDataType='', valueConstraint='', valueConstraintType='', valueShape=':b', note='Typically the author.'),
        CSVRow(
                shapeID=':b', shapeLabel='Person', shapeClosed=None, start=None, propertyID='foaf:name', propertyLabel='Name', mandatory=True, repeatable=False, valueNodeType='String', valueDataType='xsd:string', valueConstraint='', valueConstraintType='', valueShape='', note=''),
    ]
    assert type(csvreader(csvfile_name)) == list
    assert type(expected_output) == list
    assert len(csvreader(csvfile_name)) == 2
    assert len(expected_output) == 2
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
