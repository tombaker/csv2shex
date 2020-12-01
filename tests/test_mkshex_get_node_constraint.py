"""@@@"""

from ShExJSG.ShExJ import NodeConstraint, shapeExpr
from csv2shex.csvshape import CSVShape, CSVTripleConstraint
from csv2shex.mkshex import get_node_constraint


def test_mkshex_get_node_constraint_simple_dicts():
    """@@@"""
    shap = CSVShape(
        start=True,
        shapeID=":a",
        tc_list=[
            CSVTripleConstraint(propertyID="dct:creator", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="dct:subject", valueNodeType="IRI"),
            CSVTripleConstraint(propertyID="dct:date", valueNodeType="String"),
        ],
    )
    assert shap.tc_list[0].valueNodeType == "IRI"
    csv_tc_input = shap.tc_list[0]
    assert csv_tc_input.valueNodeType == "IRI"
    assert type(get_node_constraint(csv_tc_input)) == NodeConstraint


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
    assert shapes[0].tc_list[0].propertyID == "dc:creator"
