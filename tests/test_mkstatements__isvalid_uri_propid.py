"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_isvalid_property_uri_prefixed():
    """@@@"""
    stat = Statement(
        prop_id="wdt:P31",
    )
    stat._normalize_property_uri()
    assert stat._propid_is_valid_quri()


def test_mkshapes_isvalid_uristem_normal_uri():
    """@@@"""
    stat = Statement(
        prop_id="https://www.wikidata.org/wiki/Q46914185",
    )
    stat._normalize_property_uri()
    assert stat._propid_is_valid_quri()


def test_mkshapes_isvalid_property_uri_with_angle_brackets():
    """@@@"""
    stat = Statement(
        prop_id="<https://www.wikidata.org/wiki/Q46914185>",
    )
    stat._normalize_property_uri()
    assert stat._propid_is_valid_quri()


def test_mkshapes_isvalid_property_uri_colon_only():
    """@@@"""
    stat = Statement(
        prop_id=":tombaker",
    )
    stat._normalize_property_uri()
    assert stat._propid_is_valid_quri()


def test_mkshapes_isvalid_uristem_not():
    """@@@"""
    stat = Statement(
        prop_id="foobar",
    )
    stat._normalize_property_uri()
    assert not stat._propid_is_valid_quri()
