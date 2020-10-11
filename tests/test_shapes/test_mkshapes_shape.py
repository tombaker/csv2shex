"""Shape object holds statements sharing a common shape_id."""

from csv2shex.mkshapes import Shape

SHAPE_OBJECT = Shape(
    start=True,
    shape_id="@a",
    shape_statements=[
        {"prop_id": "dct:creator", "value_node_type": "URI"},
        {"prop_id": "dct:subject", "value_node_type": "URI"},
        {"prop_id": "dct:date", "value_node_type": "String"},
    ],
)


def test_shape_fields_individually_addressable():
    """Shape fields individually addressable."""
    shap = SHAPE_OBJECT
    assert shap.start
    assert shap.shape_id == "@a"
    assert shap.shape_statements[1] == {
        "prop_id": "dct:subject",
        "value_node_type": "URI",
    }


def test_shape_initialized_by_assignment():
    """Shape fields created by assignment."""
    shap = Shape()
    shap.start = True
    shap.shape_id = "@a"
    shap.shape_statements = []
    shap.shape_statements.append({"prop_id": "dct:creator", "value_node_type": "URI"})
    shap.shape_statements.append({"prop_id": "dct:subject", "value_node_type": "URI"})
    shap.shape_statements.append({"prop_id": "dct:date", "value_node_type": "String"})
    assert shap == SHAPE_OBJECT


def test_shape_initialized_with_no_propertyvalues_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = Shape()
    shap.start = True
    shap.shape_id = "@a"
    assert shap == Shape(start=True, shape_id="@a")


def test_shape_initialized_with_no_start_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = Shape()
    shap.shape_id = "@a"
    shap.shape_statements = []
    shap.shape_statements.append({"prop_id": "dct:creator", "value_node_type": "URI"})
    shap.shape_statements.append({"prop_id": "dct:subject", "value_node_type": "URI"})
    shap.shape_statements.append({"prop_id": "dct:date", "value_node_type": "String"})
    assert shap == Shape(
        shape_id="@a",
        shape_statements=[
            {"prop_id": "dct:creator", "value_node_type": "URI"},
            {"prop_id": "dct:subject", "value_node_type": "URI"},
            {"prop_id": "dct:date", "value_node_type": "String"},
        ],
    )


def test_shape_initialized_with_no_shapeid_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = Shape()
    shap.start = True
    shap.shape_statements = []
    shap.shape_statements.append({"prop_id": "dct:creator", "value_node_type": "URI"})
    shap.shape_statements.append({"prop_id": "dct:subject", "value_node_type": "URI"})
    shap.shape_statements.append({"prop_id": "dct:date", "value_node_type": "String"})
    assert shap == Shape(
        start=True,
        shape_statements=[
            {"prop_id": "dct:creator", "value_node_type": "URI"},
            {"prop_id": "dct:subject", "value_node_type": "URI"},
            {"prop_id": "dct:date", "value_node_type": "String"},
        ],
    )
