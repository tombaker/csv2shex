"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_isvalid_litpicklist():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red green yellow",
        constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist_as_list()
    assert stat._litpicklist_is_valid()


def test_mkshapes_isvalid_litpicklist_just_one_item():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="red",
        constraint_type="LitPicklist",
    )
    stat._normalize_litpicklist_as_list()
    assert stat._litpicklist_is_valid()
