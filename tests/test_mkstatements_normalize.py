"""Initialize instances of Statement."""

from csv2shex.mkstatements import Statement


def test_statement_angle_brackets_stripped_from_uristem():
    """Angle brackets stripped from URIStem 'constraint_value'."""
    shap = Statement(
        prop_id="dc:publisher",
        constraint_value="<http://ibm.com>",
        constraint_type="URIStem",
    )
    shap.self_normalize()
    assert shap.constraint_value == "http://ibm.com"
    assert shap.constraint_type == "URIStem"
