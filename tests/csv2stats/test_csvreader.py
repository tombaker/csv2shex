"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.csv2stats import csvreader, Statement

CSV_CONTENTS = """\
shapeid,prop_id,v_type
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
        { 'shapeid': '@a', 'prop_id': 'dct:creator', 'v_type': 'URI'},
        { 'shapeid': '@a', 'prop_id': 'dct:subject', 'v_type': 'URI'},
        { 'shapeid': '@a', 'prop_id': 'dct:date', 'v_type': 'String'},
    ]
