"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.csvparser import csvreader, Statement

CSV_CONTENTS = """\
shape_id,prop_id,value_type
@a,dct:creator,URI
@a,dct:subject,URI
@a,dct:date,String
"""


def test_csvreader(tmp_path):
    """@@@Docstring"""
    os.chdir(tmp_path)
    csvfile = Path(tmp_path).joinpath("some.csv")
    csvfile.write_text(CSV_CONTENTS)
    assert csvreader(csvfile) == [
        { 'shape_id': '@a', 'prop_id': 'dct:creator', 'value_type': 'URI'},
        { 'shape_id': '@a', 'prop_id': 'dct:subject', 'value_type': 'URI'},
        { 'shape_id': '@a', 'prop_id': 'dct:date', 'value_type': 'String'},
    ]
