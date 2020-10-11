"""@@@"""


import pytest
from csv2shex.mkstatements import Statement


@pytest.mark.skip
def test_mkshapes_validate_uripicklist():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        value_constraint=[":red", ":green", ":yellow"],
        constraint_type="UriPicklist",
    )
    assert stat._validate_uripicklist()


@pytest.mark.skip
def test_mkshapes_validate_uripicklist_normalized():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        value_constraint=":red :green :yellow",
        constraint_type="UriPicklist",
    )
    stat._normalize_uripicklist()
    assert stat._validate_uripicklist()


@pytest.mark.skip
def test_mkshapes_validate_uripicklist_just_one_item():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="dcterms:subject",
        value_constraint=["wd:Q46914185"],
        constraint_type="UriPicklist",
    )
    assert stat._validate_uripicklist()


def test_mkshapes_validate_uripicklist_just_one_item_normalized():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="dcterms:subject",
        value_constraint="https://www.wikidata.org/wiki/Q46914185",
        constraint_type="UriPicklist",
    )
    stat._normalize_uripicklist()
    assert stat._validate_uripicklist()
