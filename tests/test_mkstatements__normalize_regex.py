"""@@@"""


import re
from csv2shex.mkstatements import Statement


def test_mkstatements_validate_regex():
    """@@@"""
    stat = Statement(
        prop_id=":status", constraint_value="approved_*", constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.constraint_value == re.compile("approved_*")


def test_mkstatements_validate_regex_does_not_compile():
    """@@@"""
    stat = Statement(
        prop_id=":status", constraint_value="approved_(*", constraint_type="Regex",
    )
    stat._normalize_regex()
    assert not stat.constraint_value
