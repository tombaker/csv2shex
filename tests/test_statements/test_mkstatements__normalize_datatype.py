"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkstatements_normalize_datatype():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        constraint_value="xsd:string",
        constraint_type="Datatype",
    )
    stat._normalize_datatype()
    assert stat.value_type == "Literal"


def test_mkstatements_normalize_datatype_none_value_ignored():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        constraint_type="Datatype",
    )
    stat._normalize_datatype()
    assert stat.value_type == "Literal"
    assert not stat.constraint_value


def test_mkstatements_normalize_datatype_quotes_are_part():
    """@@@"""
    stat = Statement(
        prop_id=":status",
        constraint_value="confidential",
        constraint_type="Datatype",
    )
    stat._normalize_datatype()
    assert stat.value_type == "Literal"
    assert stat.constraint_value is None
