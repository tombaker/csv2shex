"""Initialize instances of CSVRow."""

from csv2shex.csvrow import CSVRow


def test_statement_angle_brackets_stripped_from_uristem():
    """Angle brackets stripped from UriStem 'valueConstraint'."""
    shap = CSVRow(
        propertyID="dc:publisher",
        valueConstraint="<http://ibm.com>",
        valueConstraintType="UriStem",
    )
    shap.normalize()
    assert shap.valueConstraint == "http://ibm.com"
    assert shap.valueConstraintType == "UriStem"
