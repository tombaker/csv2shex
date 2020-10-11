"""@@@"""


import re
from csv2shex.mkstatements import Statement


def test_mkstatements_normalize_regex():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        value_constraint="approved_*",
        value_constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.value_node_type == "Literal"
    assert stat.value_constraint == re.compile("approved_*")


def test_mkstatements_normalize_regex_does_not_compile():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        value_constraint="approved_(*",
        value_constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.value_node_type == "Literal"
    assert not stat.value_constraint


def test_mkstatements_normalize_regex_none_value_ignored():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        value_constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.value_node_type == "Literal"
    assert not stat.value_constraint


def test_mkstatements_normalize_regex_forward_slashes_are_part():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        value_constraint="/approved_*/",
        value_constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.value_node_type == "Literal"
    assert stat.value_constraint == re.compile("/approved_*/")


def test_mkstatements_normalize_regex_blanks_are_part():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        value_constraint="^2020 August",
        value_constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.value_node_type == "Literal"
    assert stat.value_constraint == re.compile("^2020 August")


def test_mkstatements_normalize_regex_quotes_are_part():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        value_constraint="'confidential'",
        value_constraint_type="Regex",
    )
    stat._normalize_regex()
    assert stat.value_node_type == "Literal"
    assert stat.value_constraint == re.compile("'confidential'")
