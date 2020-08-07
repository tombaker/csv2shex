"""Sanity check for URI as value_type."""


from csv2shex.mkstatements import Statement


def test_mkshapes_isvalid_uri_value_type_quri():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        value_type="URI",
        constraint_value="wd:",
    )
    assert statement._value_type_uri_is_valid_quri()


def test_mkshapes_isvalid_value_type_normal_uri():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        value_type="URI",
        constraint_value="http://www.gmd.de/",
    )
    assert statement._value_type_uri_is_valid_quri()


def test_mkshapes_isvalid_value_type_uri_with_angle_brackets():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        value_type="URI",
        constraint_value="<http://www.gmd.de/>",
    )
    statement._normalize_value_type_uri()
    assert statement._value_type_uri_is_valid_quri()


def test_mkshapes_isvalid_value_type_quri_colon_only():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        value_type="URI",
        constraint_value=":",
    )
    statement._normalize_value_type_uri()
    assert statement._value_type_uri_is_valid_quri()


def test_mkshapes_isvalid_uri_as_value_type_is_not_valid_uri():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        value_type="URI",
        constraint_value="foobar",
    )
    statement._normalize_value_type_uri()
    assert not statement._value_type_uri_is_valid_quri()
