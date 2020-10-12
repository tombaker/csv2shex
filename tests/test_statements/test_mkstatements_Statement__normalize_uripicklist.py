"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_normalize_litpicklist():
    """@@@"""
    stat = Statement(
        propertyID="wdt:P31",
        value_constraint="red green yellow",
        value_constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat.value_constraint == ["red", "green", "yellow"]


def test_mkshapes_normalize_litpicklist_just_one_item():
    """@@@"""
    stat = Statement(
        propertyID="wdt:P31",
        value_constraint="red",
        value_constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat.value_constraint == ["red"]
