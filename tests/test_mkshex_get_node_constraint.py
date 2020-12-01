"""@@@"""

from csv2shex.csvshape import CSVShape, CSVTripleConstraint


def test_mkshex_get_node_constraint_simple_dicts():
    """@@@"""
    shap = CSVShape(
        start=True,
        shapeID=":a",
        tc_list=[
            {"propertyID": "dct:creator", "valueNodeType": "IRI"},
            {"propertyID": "dct:subject", "valueNodeType": "IRI"},
            {"propertyID": "dct:date", "valueNodeType": "String"},
        ],
    )
    assert shap.tc_list[0]["valueNodeType"] == "IRI"


def test_mkshex_get_node_constraint():
    """@@@"""
    shapes = [
        CSVShape(
            shapeID=":default",
            start=True,
            tc_list=[
                CSVTripleConstraint(propertyID="dc:creator"),
                CSVTripleConstraint(propertyID="dc:type"),
            ],
        )
    ]
    assert shapes[0].tc_list[0].propertyID== "dc:creator"


