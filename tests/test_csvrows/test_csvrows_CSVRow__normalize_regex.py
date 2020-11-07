"""@@@"""


import re
from csv2shex.csvrow import CSVRow


def test_csvrow_normalize_regex():
    """@@@"""
    stat = CSVRow(
        propertyID=":status",
        valueConstraint="approved_*",
        valueConstraintType="Regex",
    )
    stat._normalize_regex()
    assert stat.valueNodeType == "Literal"
    assert stat.valueConstraint == re.compile("approved_*")


def test_csvrow_normalize_regex_does_not_compile():
    """@@@"""
    stat = CSVRow(
        propertyID=":status",
        valueConstraint="approved_(*",
        valueConstraintType="Regex",
    )
    stat._normalize_regex()
    assert stat.valueNodeType == "Literal"
    assert not stat.valueConstraint


def test_csvrow_normalize_regex_none_value_ignored():
    """@@@"""
    stat = CSVRow(
        propertyID=":status",
        valueConstraintType="Regex",
    )
    stat._normalize_regex()
    assert stat.valueNodeType == "Literal"
    assert not stat.valueConstraint


def test_csvrow_normalize_regex_forward_slashes_are_part():
    """@@@"""
    stat = CSVRow(
        propertyID=":status",
        valueConstraint="/approved_*/",
        valueConstraintType="Regex",
    )
    stat._normalize_regex()
    assert stat.valueNodeType == "Literal"
    assert stat.valueConstraint == re.compile("/approved_*/")


def test_csvrow_normalize_regex_blanks_are_part():
    """@@@"""
    stat = CSVRow(
        propertyID=":status",
        valueConstraint="^2020 August",
        valueConstraintType="Regex",
    )
    stat._normalize_regex()
    assert stat.valueNodeType == "Literal"
    assert stat.valueConstraint == re.compile("^2020 August")


def test_csvrow_normalize_regex_quotes_are_part():
    """@@@"""
    stat = CSVRow(
        propertyID=":status",
        valueConstraint="'confidential'",
        valueConstraintType="Regex",
    )
    stat._normalize_regex()
    assert stat.valueNodeType == "Literal"
    assert stat.valueConstraint == re.compile("'confidential'")
