"""@@@"""


import pytest
from csv2shex.csvrows import CSVRow


@pytest.mark.skip
def test_csvshapes_validate_uripicklist():
    """@@@"""
    stat = CSVRow(
        shapeID="@default",
        propertyID="wdt:P31",
        valueConstraint=[":red", ":green", ":yellow"],
        valueConstraintType="UriPicklist",
    )
    assert stat._validate_uripicklist()


@pytest.mark.skip
def test_csvshapes_validate_uripicklist_normalized():
    """@@@"""
    stat = CSVRow(
        shapeID="@default",
        propertyID="wdt:P31",
        valueConstraint=":red :green :yellow",
        valueConstraintType="UriPicklist",
    )
    stat._normalize_uripicklist()
    assert stat._validate_uripicklist()


@pytest.mark.skip
def test_csvshapes_validate_uripicklist_just_one_item():
    """@@@"""
    stat = CSVRow(
        shapeID="@default",
        propertyID="dcterms:subject",
        valueConstraint=["wd:Q46914185"],
        valueConstraintType="UriPicklist",
    )
    assert stat._validate_uripicklist()


def test_csvshapes_validate_uripicklist_just_one_item_normalized():
    """@@@"""
    stat = CSVRow(
        shapeID="@default",
        propertyID="dcterms:subject",
        valueConstraint="https://www.wikidata.org/wiki/Q46914185",
        valueConstraintType="UriPicklist",
    )
    stat._normalize_uripicklist()
    assert stat._validate_uripicklist()
