"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.csvparser import csvreader, Statement

CSV_CONTENTS = """\
shape_id,prop_id,value_type
@photo,dcterms:creator,URI
@photo,dcterms:subject,URI
@photo,dcterms:date,String
"""


def test_csvreader(tmp_path):
    """@@@Docstring"""
    os.chdir(tmp_path)
    csvfile = Path(tmp_path).joinpath("some.csv")
    csvfile.write_text(CSV_CONTENTS)
    assert csvreader(csvfile) == [
        { 'shape_id': '@photo', 'prop_id': 'dcterms:creator', 'value_type': 'URI'},
        { 'shape_id': '@photo', 'prop_id': 'dcterms:subject', 'value_type': 'URI'},
        { 'shape_id': '@photo', 'prop_id': 'dcterms:date', 'value_type': 'String'},
    ]
