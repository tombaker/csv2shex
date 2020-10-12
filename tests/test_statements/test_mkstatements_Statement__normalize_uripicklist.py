"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_normalize_litpicklist():
    """@@@"""
    stat = Statement(
        propertyID="wdt:P31",
        valueConstraint="red green yellow",
        valueConstraintType="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat.valueConstraint == ["red", "green", "yellow"]


def test_mkshapes_normalize_litpicklist_just_one_item():
    """@@@"""
    stat = Statement(
        propertyID="wdt:P31",
        valueConstraint="red",
        valueConstraintType="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat.valueConstraint == ["red"]
