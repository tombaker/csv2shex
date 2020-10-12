"""Sanity check for URI as value_node_type."""


from csv2shex.mkstatements import Statement


def test_mkshapes_validate_uri_value_node_type_quri():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        prop_id="wdt:P31",
        value_node_type="URI",
        value_constraint="wd:",
    )
    assert statement._validate_valueuri()


def test_mkshapes_validate_value_node_type_normal_uri():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        prop_id="wdt:P31",
        value_node_type="URI",
        value_constraint="http://www.gmd.de/",
    )
    assert statement._validate_valueuri()


def test_mkshapes_validate_value_node_type_uri_with_angle_brackets():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        prop_id="wdt:P31",
        value_node_type="URI",
        value_constraint="<http://www.gmd.de/>",
    )
    statement._normalize_valueuri()
    assert statement._validate_valueuri()


def test_mkshapes_validate_value_node_type_quri_colon_only():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        prop_id="wdt:P31",
        value_node_type="URI",
        value_constraint=":",
    )
    statement._normalize_valueuri()
    assert statement._validate_valueuri()


def test_mkshapes_validate_uri_as_value_node_type_is_not_valid_uri():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        prop_id="wdt:P31",
        value_node_type="URI",
        value_constraint="foobar",
    )
    statement._normalize_valueuri()
    assert not statement._validate_valueuri()