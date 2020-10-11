"""Initialize instances of Statement."""

from csv2shex.mkstatements import Statement


def test_statement_angle_brackets_stripped_from_uristem():
    """Angle brackets stripped from UriStem 'value_constraint'."""
    shap = Statement(
        prop_id="dc:publisher",
        value_constraint="<http://ibm.com>",
        constraint_type="UriStem",
    )
    shap.normalize()
    assert shap.value_constraint == "http://ibm.com"
    assert shap.constraint_type == "UriStem"
