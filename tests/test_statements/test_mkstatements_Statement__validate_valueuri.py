"""Sanity check for URI as valueNodeType."""


from csv2shex.mkstatements import Statement


def test_mkshapes_validate_uri_valueNodeType_quri():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        valueNodeType="URI",
        value_constraint="wd:",
    )
    assert statement._validate_valueuri()


def test_mkshapes_validate_valueNodeType_normal_uri():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        valueNodeType="URI",
        value_constraint="http://www.gmd.de/",
    )
    assert statement._validate_valueuri()


def test_mkshapes_validate_valueNodeType_uri_with_angle_brackets():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        valueNodeType="URI",
        value_constraint="<http://www.gmd.de/>",
    )
    statement._normalize_valueuri()
    assert statement._validate_valueuri()


def test_mkshapes_validate_valueNodeType_quri_colon_only():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        valueNodeType="URI",
        value_constraint=":",
    )
    statement._normalize_valueuri()
    assert statement._validate_valueuri()


def test_mkshapes_validate_uri_as_valueNodeType_is_not_valid_uri():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        valueNodeType="URI",
        value_constraint="foobar",
    )
    statement._normalize_valueuri()
    assert not statement._validate_valueuri()
