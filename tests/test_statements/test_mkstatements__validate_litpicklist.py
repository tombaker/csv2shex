"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_validate_litpicklist():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red green yellow",
        constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat._validate_litpicklist()


def test_mkshapes_validate_litpicklist_just_one_item():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="red",
        constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat._validate_litpicklist()
