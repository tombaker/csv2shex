"""@@@"""


import re
from csv2shex.mkstatements import Statement


def test_mkstatements_validate_regex():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        constraint_value="approved_*",
        constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.constraint_value == re.compile("approved_*")


def test_mkstatements_validate_regex_does_not_compile():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        constraint_value="approved_(*",
        constraint_type="Regex",
    )
    stat._normalize_regex()
    assert not stat.constraint_value


def test_mkstatements_validate_regex_none_value_ignored():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        constraint_type="Regex",
    )
    stat._normalize_regex()
    assert not stat.constraint_value


def test_mkstatements_validate_regex_forward_slashes_are_part():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        constraint_value="/approved_*/",
        constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.constraint_value == re.compile("/approved_*/")


def test_mkstatements_validate_regex_blanks_are_part():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        constraint_value="^2020 August",
        constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.constraint_value == re.compile("^2020 August")
