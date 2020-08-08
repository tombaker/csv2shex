"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_normalize_litpicklist_as_list():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red green yellow",
        constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist_as_list()
    assert stat.constraint_value == ["red", "green", "yellow"]


def test_mkshapes_normalize_litpicklist_as_list_just_one_item():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red",
        constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist_as_list()
    assert stat.constraint_value == ["red"]


def test_mkshapes_normalize_litpicklist_as_list():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red green yellow",
        constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist_as_list()
    assert stat.constraint_value == ["red", "green", "yellow"]


def test_mkshapes_normalize_litpicklist_as_list_just_one_item():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red",
        constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist_as_list()
    assert stat.constraint_value == ["red"]
