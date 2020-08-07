"""Check CSV file structure for anomalies"""


from csv2shex.mkstatements import Statement


def test_mkshapes_isvalid_uristem_is_uri_prefix():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="wd:",
        constraint_type="URIStem",
    )
    assert statement._uristem_is_used_correctly()


def test_mkshapes_isvalid_uristem_is_url():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="http://www.gmd.de/",
        constraint_type="URIStem",
    )
    assert statement._uristem_is_used_correctly()


def test_mkshapes_isvalid_uristem_is_url_with_angle_brackets():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="<http://www.gmd.de/>",
        constraint_type="URIStem",
    )
    statement._normalize_uristem_stripping_angle_brackets()
    assert statement._uristem_is_used_correctly()


def test_mkshapes_isvalid_uristem_is_not_valid_URL():
    """@@@"""
    statement = Statement(
        shape_id="@default",
        prop_id="wdt:P31",
        constraint_value="foobar",
        constraint_type="URIStem",
    )
    statement._normalize_uristem_stripping_angle_brackets()
    assert not statement._uristem_is_used_correctly()
