"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_isvalid_uripicklist():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value=["red", "green", "yellow"],
        constraint_type="UriPicklist",
    )
    assert stat._uripicklist_is_valid()


def test_mkshapes_isvalid_uripicklist_just_one_item():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value=["red"],
        constraint_type="UriPicklist",
    )
    assert stat._uripicklist_is_valid()
def test_mkshapes_isvalid_uripicklist():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
        constraint_value="red green yellow",
        constraint_type="LitPicklist",
    )
    stat._normalize_uripicklist_as_list()
    assert stat._uripicklist_is_valid()


def test_mkshapes_isvalid_uripicklist_just_one_item():
    """@@@"""
    stat = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="red",
        constraint_type="LitPicklist",
    )
    stat._normalize_uripicklist_as_list()
    assert stat._uripicklist_is_valid()


