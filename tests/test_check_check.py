"""Check CSV file structure for anomalies"""


import os
import pytest
from pathlib import Path

# from csv2shex.check import check
from csv2shex.mkstatements import csvreader, list_statements


@pytest.mark.skip
def test_check(tmp_path):
    """Check CSV file structure for anomalies"""
    os.chdir(tmp_path)
    csvfile = Path(tmp_path).joinpath("some.csv")
    csvfile.write_text(
        (
            "prop_id,value_type,constraint_type,constraint_value\n"
            "wdt:P31,URI,URIStem,wd:\n"
        )
    )
    for statement in list_statements(csvreader(csvfile)):
        assert statement._is_uristem_used_correctly()
