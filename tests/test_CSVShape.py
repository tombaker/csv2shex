"""CSVShape object holds statements sharing a common shapeID."""

from csv2shex.csvshape import CSVShape

SHAPE_OBJECT = CSVShape(
    start=True,
    shapeID=":a",
    tripleconstraints_list=[
        {"propertyID": "dct:creator", "valueNodeType": "URI"},
        {"propertyID": "dct:subject", "valueNodeType": "URI"},
        {"propertyID": "dct:date", "valueNodeType": "String"},
    ],
)


def test_shape_fields_are_individually_addressable():
    """Fields of CSVShape instance are individually addressable."""
    shap = SHAPE_OBJECT
    assert shap.start
    assert shap.shapeID == ":a"
    assert shap.tripleconstraints_list[1] == {"propertyID": "dct:subject", "valueNodeType": "URI"}
    assert len(shap.tripleconstraints_list) == 3


def test_tripleconstraints_list_items_are_individually_addressable():
    """Items in tripleconstraints_list field of CSVShape instance are individually addressable."""
    shap = SHAPE_OBJECT
    assert shap.tripleconstraints_list[1]["propertyID"] == "dct:subject"
    assert shap.tripleconstraints_list[2]["valueNodeType"] == "String"


def test_shape_initialized_by_assignment():
    """CSVShape instances can be created by assignment."""
    shap = CSVShape()
    shap.start = True
    shap.shapeID = ":a"
    shap.tripleconstraints_list = []
    shap.tripleconstraints_list.append({"propertyID": "dct:creator", "valueNodeType": "URI"})
    shap.tripleconstraints_list.append({"propertyID": "dct:subject", "valueNodeType": "URI"})
    shap.tripleconstraints_list.append({"propertyID": "dct:date", "valueNodeType": "String"})
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
    shap.tripleconstraints_list = []
    shap.tripleconstraints_list.append({"propertyID": "dct:creator", "valueNodeType": "URI"})
    shap.tripleconstraints_list.append({"propertyID": "dct:subject", "valueNodeType": "URI"})
    shap.tripleconstraints_list.append({"propertyID": "dct:date", "valueNodeType": "String"})
    assert shap == CSVShape(
        shapeID=":a",
        tripleconstraints_list=[
            {"propertyID": "dct:creator", "valueNodeType": "URI"},
            {"propertyID": "dct:subject", "valueNodeType": "URI"},
            {"propertyID": "dct:date", "valueNodeType": "String"},
        ],
    )


def test_shape_initialized_with_no_shapeid_field_should_pass_for_now():
    """Test should pass for now but this condition should raise exception."""
    shap = CSVShape()
    shap.start = True
    shap.tripleconstraints_list = []
    shap.tripleconstraints_list.append({"propertyID": "dct:creator", "valueNodeType": "URI"})
    shap.tripleconstraints_list.append({"propertyID": "dct:subject", "valueNodeType": "URI"})
    shap.tripleconstraints_list.append({"propertyID": "dct:date", "valueNodeType": "String"})
    assert shap == CSVShape(
        start=True,
        tripleconstraints_list=[
            {"propertyID": "dct:creator", "valueNodeType": "URI"},
            {"propertyID": "dct:subject", "valueNodeType": "URI"},
            {"propertyID": "dct:date", "valueNodeType": "String"},
        ],
    )
