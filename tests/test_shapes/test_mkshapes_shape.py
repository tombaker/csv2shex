"""Shape object holds statements sharing a common shapeID."""

from csv2shex.mkshapes import Shape

SHAPE_OBJECT = Shape(
    start=True,
    shapeID="@a",
    shape_statements=[
        {"propertyID": "dct:creator", "value_node_type": "URI"},
        {"propertyID": "dct:subject", "value_node_type": "URI"},
        {"propertyID": "dct:date", "value_node_type": "String"},
    ],
)


def test_shape_fields_individually_addressable():
    """Shape fields individually addressable."""
    shap = SHAPE_OBJECT
    assert shap.start
    assert shap.shapeID == "@a"
    assert shap.shape_statements[1] == {
        "propertyID": "dct:subject",
        "value_node_type": "URI",
    }


def test_shape_initialized_by_assignment():
    """Shape fields created by assignment."""
    shap = Shape()
    shap.start = True
    shap.shapeID = "@a"
    shap.shape_statements = []
    shap.shape_statements.append({"propertyID": "dct:creator", "value_node_type": "URI"})
    shap.shape_statements.append({"propertyID": "dct:subject", "value_node_type": "URI"})
    shap.shape_statements.append({"propertyID": "dct:date", "value_node_type": "String"})
    assert shap == SHAPE_OBJECT


def test_shape_initialized_with_no_propertyvalues_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = Shape()
    shap.start = True
    shap.shapeID = "@a"
    assert shap == Shape(start=True, shapeID="@a")


def test_shape_initialized_with_no_start_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = Shape()
    shap.shapeID = "@a"
    shap.shape_statements = []
    shap.shape_statements.append({"propertyID": "dct:creator", "value_node_type": "URI"})
    shap.shape_statements.append({"propertyID": "dct:subject", "value_node_type": "URI"})
    shap.shape_statements.append({"propertyID": "dct:date", "value_node_type": "String"})
    assert shap == Shape(
        shapeID="@a",
        shape_statements=[
            {"propertyID": "dct:creator", "value_node_type": "URI"},
            {"propertyID": "dct:subject", "value_node_type": "URI"},
            {"propertyID": "dct:date", "value_node_type": "String"},
        ],
    )


def test_shape_initialized_with_no_shapeid_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = Shape()
    shap.start = True
    shap.shape_statements = []
    shap.shape_statements.append({"propertyID": "dct:creator", "value_node_type": "URI"})
    shap.shape_statements.append({"propertyID": "dct:subject", "value_node_type": "URI"})
    shap.shape_statements.append({"propertyID": "dct:date", "value_node_type": "String"})
    assert shap == Shape(
        start=True,
        shape_statements=[
            {"propertyID": "dct:creator", "value_node_type": "URI"},
            {"propertyID": "dct:subject", "value_node_type": "URI"},
            {"propertyID": "dct:date", "value_node_type": "String"},
        ],
    )
