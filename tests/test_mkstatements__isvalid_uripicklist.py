"""@@@"""


import pytest
from csv2shex.mkstatements import Statement


@pytest.mark.skip
def test_mkshapes_isvalid_uripicklist():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value=[":red", ":green", ":yellow"],
        constraint_type="UriPicklist",
    )
    assert stat._uripicklist_is_valid()


@pytest.mark.skip
def test_mkshapes_isvalid_uripicklist_normalized():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value=":red :green :yellow",
        constraint_type="UriPicklist",
    )
    stat._normalize_uripicklist_as_list()
    assert stat._uripicklist_is_valid()


@pytest.mark.skip
def test_mkshapes_isvalid_uripicklist_just_one_item():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="dcterms:subject",
        constraint_value=["wd:Q46914185"],
        constraint_type="UriPicklist",
    )
    assert stat._uripicklist_is_valid()


def test_mkshapes_isvalid_uripicklist_just_one_item_normalized():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="dcterms:subject",
        constraint_value="https://www.wikidata.org/wiki/Q46914185",
        constraint_type="UriPicklist",
    )
    stat._normalize_uripicklist_as_list()
    assert stat._uripicklist_is_valid()
