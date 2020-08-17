"""Initialize instances of Statement."""

from csv2shex.mkstatements import Statement


def test_statement_angle_brackets_stripped_from_uristem():
    """Angle brackets stripped from UriStem 'constraint_value'."""
    shap = Statement(
        prop_id="dc:publisher",
        constraint_value="<http://ibm.com>",
        constraint_type="UriStem",
    )
    shap.normalize()
    assert shap.constraint_value == "http://ibm.com"
    assert shap.constraint_type == "UriStem"
