"""Check CSV file structure for anomalies"""


from csv2shex.mkstatements import Statement


def test_mkshapes_isvalid_uristem_uri_prefix():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="wd:",
        constraint_type="URIStem",
    )
    assert statement._uristem_is_valid_quri()


def test_mkshapes_isvalid_uristem_normal_uri():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="http://www.gmd.de/",
        constraint_type="URIStem",
    )
    assert statement._uristem_is_valid_quri()


def test_mkshapes_isvalid_uristem_uri_with_angle_brackets():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="<http://www.gmd.de/>",
        constraint_type="URIStem",
    )
    statement._normalize_uristem_uri()
    assert statement._uristem_is_valid_quri()


def test_mkshapes_isvalid_uristem_not():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="foobar",
        constraint_type="URIStem",
    )
    statement._normalize_uristem_uri()
    assert not statement._uristem_is_valid_quri()
