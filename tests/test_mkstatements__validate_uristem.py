"""Check CSV file structure for anomalies"""


from csv2shex.mkstatements import Statement


def test_mkshapes_validate_uristem_prefixed():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="wd:",
        constraint_type="UriStem",
    )
    assert statement._validate_uristem()


def test_mkshapes_validate_uristem_normal_uri():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="http://www.gmd.de/",
        constraint_type="UriStem",
    )
    assert statement._validate_uristem()


def test_mkshapes_validate_uristem_with_angle_brackets():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="<http://www.gmd.de/>",
        constraint_type="UriStem",
    )
    statement._normalize_uristem()
    assert statement._validate_uristem()


def test_mkshapes_validate_uristem_colon_only():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value=":",
        constraint_type="UriStem",
    )
    statement._normalize_uristem()
    assert statement._validate_uristem()


def test_mkshapes_validate_uristem_not():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="foobar",
        constraint_type="UriStem",
    )
    statement._normalize_uristem()
    assert not statement._validate_uristem()
