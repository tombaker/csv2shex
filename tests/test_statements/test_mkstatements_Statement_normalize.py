"""Initialize instances of Statement."""

from csv2shex.mkstatements import Statement


def test_statement_angle_brackets_stripped_from_uristem():
    """Angle brackets stripped from UriStem 'value_constraint'."""
    shap = Statement(
        propertyID="dc:publisher",
        value_constraint="<http://ibm.com>",
        valueConstraintType="UriStem",
    )
    shap.normalize()
    assert shap.value_constraint == "http://ibm.com"
    assert shap.valueConstraintType == "UriStem"
