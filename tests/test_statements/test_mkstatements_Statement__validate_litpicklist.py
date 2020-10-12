"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_validate_litpicklist():
    """@@@"""
    stat = Statement(
        propertyID="wdt:P31",
        valueConstraint="red green yellow",
        valueConstraintType="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat._validate_litpicklist()


def test_mkshapes_validate_litpicklist_just_one_item():
    """@@@"""
    stat = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        valueConstraint="red",
        valueConstraintType="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat._validate_litpicklist()
