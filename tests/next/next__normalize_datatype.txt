"""@@@"""


from csv2shex.csvrow import CSVRow


def test_csvrow_normalize_datatype():
    """@@@"""
    stat = CSVRow(
        propertyID=":status",
        valueConstraint="xsd:string",
        valueConstraintType="Datatype",
    )
    stat._normalize_datatype()
    assert stat.valueNodeType == "Literal"


def test_csvrow_normalize_datatype_none_value_ignored():
    """@@@"""
    stat = CSVRow(
        propertyID=":status",
        valueConstraintType="Datatype",
    )
    stat._normalize_datatype()
    assert stat.valueNodeType == "Literal"
    assert not stat.valueConstraint


def test_csvrow_normalize_datatype_quotes_are_part():
    """@@@"""
    stat = CSVRow(
        propertyID=":status",
        valueConstraint="confidential",
        valueConstraintType="Datatype",
    )
    stat._normalize_datatype()
    assert stat.valueNodeType == "Literal"
    assert stat.valueConstraint is None
