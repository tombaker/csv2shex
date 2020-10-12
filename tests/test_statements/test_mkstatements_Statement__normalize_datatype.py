"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkstatements_normalize_datatype():
    """@@@"""
    stat = Statement(
        propertyID=":status",
        value_constraint="xsd:string",
        valueConstraintType="Datatype",
    )
    stat._normalize_datatype()
    assert stat.valueNodeType == "Literal"


def test_mkstatements_normalize_datatype_none_value_ignored():
    """@@@"""
    stat = Statement(
        propertyID=":status",
        valueConstraintType="Datatype",
    )
    stat._normalize_datatype()
    assert stat.valueNodeType == "Literal"
    assert not stat.value_constraint


def test_mkstatements_normalize_datatype_quotes_are_part():
    """@@@"""
    stat = Statement(
        propertyID=":status",
        value_constraint="confidential",
        valueConstraintType="Datatype",
    )
    stat._normalize_datatype()
    assert stat.valueNodeType == "Literal"
    assert stat.value_constraint is None
