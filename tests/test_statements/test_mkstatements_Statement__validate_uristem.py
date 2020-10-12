"""Check CSV file structure for anomalies"""


from csv2shex.mkstatements import Statement


def test_mkshapes_validate_uristem_prefixed():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        value_constraint="wd:",
        value_constraint_type="UriStem",
    )
    assert statement._validate_uristem()


def test_mkshapes_validate_uristem_normal_uri():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        value_constraint="http://www.gmd.de/",
        value_constraint_type="UriStem",
    )
    assert statement._validate_uristem()


def test_mkshapes_validate_uristem_with_angle_brackets():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        value_constraint="<http://www.gmd.de/>",
        value_constraint_type="UriStem",
    )
    statement._normalize_uristem()
    assert statement._validate_uristem()


def test_mkshapes_validate_uristem_colon_only():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        value_constraint=":",
        value_constraint_type="UriStem",
    )
    statement._normalize_uristem()
    assert statement._validate_uristem()


def test_mkshapes_validate_uristem_not():
    """@@@"""
    statement = Statement(
        shapeID="@default",
        propertyID="wdt:P31",
        value_constraint="foobar",
        value_constraint_type="UriStem",
    )
    statement._normalize_uristem()
    assert not statement._validate_uristem()
