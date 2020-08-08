"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_isvalid_literal_picklist():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red green yellow",
        constraint_type="LitPicklist",
    )
    stat._normalize_literal_picklist()
    assert stat._literal_picklist_is_valid()


def test_mkshapes_isvalid_literal_picklist_just_one_item():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="red",
        constraint_type="LitPicklist",
    )
    stat._normalize_literal_picklist()
    assert stat._literal_picklist_is_valid()


def test_mkshapes_normalize_literal_picklist():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red green yellow",
        constraint_type="LitPicklist",
    )
    stat._normalize_literal_picklist()
    assert stat.constraint_value == ["red", "green", "yellow"]


def test_mkshapes_normalize_literal_picklist_just_one_item():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red",
        constraint_type="LitPicklist",
    )
    stat._normalize_literal_picklist()
    assert stat.constraint_value == ["red"]
