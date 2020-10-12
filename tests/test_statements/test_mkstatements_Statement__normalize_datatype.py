"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkstatements_normalize_datatype():
    """@@@"""
    stat = Statement(
        propertyID=":status",
        valueConstraint="xsd:string",
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
    assert not stat.valueConstraint


def test_mkstatements_normalize_datatype_quotes_are_part():
    """@@@"""
    stat = Statement(
        propertyID=":status",
        valueConstraint="confidential",
        valueConstraintType="Datatype",
    )
    stat._normalize_datatype()
    assert stat.valueNodeType == "Literal"
    assert stat.valueConstraint is None
