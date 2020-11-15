"""CSVShape object holds statements sharing a common shapeID."""

from csv2shex.csvshape import CSVShape

SHAPE_OBJECT = CSVShape(
    start=True,
    shapeID=":a",
    pvdicts_list=[
        {"propertyID": "dct:creator", "valueNodeType": "URI"},
        {"propertyID": "dct:subject", "valueNodeType": "URI"},
        {"propertyID": "dct:date", "valueNodeType": "String"},
    ],
)


def test_shape_fields_individually_addressable():
    """CSVShape fields individually addressable."""
    shap = SHAPE_OBJECT
    assert shap.start
    assert shap.shapeID == ":a"
    assert shap.pvdicts_list[1] == {
        "propertyID": "dct:subject",
        "valueNodeType": "URI",
    }


def test_shape_initialized_by_assignment():
    """CSVShape fields created by assignment."""
    shap = CSVShape()
    shap.start = True
    shap.shapeID = ":a"
    shap.pvdicts_list = []
    shap.pvdicts_list.append(
        {"propertyID": "dct:creator", "valueNodeType": "URI"}
    )
    shap.pvdicts_list.append(
        {"propertyID": "dct:subject", "valueNodeType": "URI"}
    )
    shap.pvdicts_list.append(
        {"propertyID": "dct:date", "valueNodeType": "String"}
    )
    assert shap == SHAPE_OBJECT


def test_shape_initialized_with_no_propertyvalues_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = CSVShape()
    shap.start = True
    shap.shapeID = ":a"
    assert shap == CSVShape(start=True, shapeID=":a")


def test_shape_initialized_with_no_start_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = CSVShape()
    shap.shapeID = ":a"
    shap.pvdicts_list = []
    shap.pvdicts_list.append(
        {"propertyID": "dct:creator", "valueNodeType": "URI"}
    )
    shap.pvdicts_list.append(
        {"propertyID": "dct:subject", "valueNodeType": "URI"}
    )
    shap.pvdicts_list.append(
        {"propertyID": "dct:date", "valueNodeType": "String"}
    )
    assert shap == CSVShape(
        shapeID=":a",
        pvdicts_list=[
            {"propertyID": "dct:creator", "valueNodeType": "URI"},
            {"propertyID": "dct:subject", "valueNodeType": "URI"},
            {"propertyID": "dct:date", "valueNodeType": "String"},
        ],
    )


def test_shape_initialized_with_no_shapeid_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = CSVShape()
    shap.start = True
    shap.pvdicts_list = []
    shap.pvdicts_list.append(
        {"propertyID": "dct:creator", "valueNodeType": "URI"}
    )
    shap.pvdicts_list.append(
        {"propertyID": "dct:subject", "valueNodeType": "URI"}
    )
    shap.pvdicts_list.append(
        {"propertyID": "dct:date", "valueNodeType": "String"}
    )
    assert shap == CSVShape(
        start=True,
        pvdicts_list=[
            {"propertyID": "dct:creator", "valueNodeType": "URI"},
            {"propertyID": "dct:subject", "valueNodeType": "URI"},
            {"propertyID": "dct:date", "valueNodeType": "String"},
        ],
    )
