"""Initialize instances of Statement."""

from csv2shex.mkstatements import Statement


def test_statement_angle_brackets_stripped_from_uristem():
    """Angle brackets stripped from UriStem 'valueConstraint'."""
    shap = Statement(
        propertyID="dc:publisher",
        valueConstraint="<http://ibm.com>",
        valueConstraintType="UriStem",
    )
    shap.normalize()
    assert shap.valueConstraint == "http://ibm.com"
    assert shap.valueConstraintType == "UriStem"
