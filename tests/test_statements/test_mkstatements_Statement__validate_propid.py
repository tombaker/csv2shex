"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_validate_property_uri_prefixed():
    """@@@"""
    stat = Statement(
        propertyID="wdt:P31",
    )
    stat._normalize_propid()
    assert stat._validate_propid()


def test_mkshapes_validate_uristem_normal_uri():
    """@@@"""
    stat = Statement(
        propertyID="https://www.wikidata.org/wiki/Q46914185",
    )
    stat._normalize_propid()
    assert stat._validate_propid()


def test_mkshapes_validate_property_uri_with_angle_brackets():
    """@@@"""
    stat = Statement(
        propertyID="<https://www.wikidata.org/wiki/Q46914185>",
    )
    stat._normalize_propid()
    assert stat._validate_propid()


def test_mkshapes_validate_property_uri_colon_only():
    """@@@"""
    stat = Statement(
        propertyID=":tombaker",
    )
    stat._normalize_propid()
    assert stat._validate_propid()


def test_mkshapes_validate_uristem_not():
    """@@@"""
    stat = Statement(
        propertyID="foobar",
    )
    stat._normalize_propid()
    assert not stat._validate_propid()
