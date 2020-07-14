"""Check CSV file structure for anomalies"""


import pytest
from csv2shex.mkstatements import Statement


@pytest.mark.skip
def test_check():
    """Check CSV file structure for anomalies."""
    statement = Statement(
        start=True,
        shape_id="@default",
        shape_label=None,
        prop_id="wdt:P31",
        prop_label=None,
        mand=None,
        repeat=None,
        value_type="URI",
        value_datatype=None,
        constraint_value="wd:",
        constraint_type="URIStem",
        shape_ref=None,
        annot=None,
    )
    assert statement._is_uristem_used_correctly()
