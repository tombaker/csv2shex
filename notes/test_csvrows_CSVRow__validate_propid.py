"""@@@"""

import pytest
from csv2shex.csvrow import CSVRow


def test_csvshape_validate_property_uri_prefixed():
    """@@@"""
    stat = CSVRow(propertyID="wdt:P31")
    stat._normalize_propid()
    assert stat._validate_propid()


def test_csvshape_validate_uristem_normal_uri():
    """@@@"""
    stat = CSVRow(propertyID="https://www.wikidata.org/wiki/Q46914185")
    stat._normalize_propid()
    assert stat._validate_propid()


def test_csvshape_validate_property_uri_with_angle_brackets():
    """@@@"""
    stat = CSVRow(propertyID="<https://www.wikidata.org/wiki/Q46914185>")
    stat._normalize_propid()
    assert stat._validate_propid()


def test_csvshape_validate_property_uri_colon_only():
    """@@@"""
    stat = CSVRow(propertyID=":tombaker")
    stat._normalize_propid()
    assert stat._validate_propid()


def test_csvshape_validate_propertyid_not_prefixed_uri_emits_warning():
    """Emits warning (and returns False) if propertyID is not a prefixed URI."""
    stat = CSVRow(propertyID="foobar")
    assert not stat._validate_propid()
