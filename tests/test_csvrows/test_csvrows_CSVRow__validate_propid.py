"""@@@"""


from csv2shex.csvrows import CSVRow


def test_csvshapes_validate_property_uri_prefixed():
    """@@@"""
    stat = CSVRow(
        propertyID="wdt:P31",
    )
    stat._normalize_propid()
    assert stat._validate_propid()


def test_csvshapes_validate_uristem_normal_uri():
    """@@@"""
    stat = CSVRow(
        propertyID="https://www.wikidata.org/wiki/Q46914185",
    )
    stat._normalize_propid()
    assert stat._validate_propid()


def test_csvshapes_validate_property_uri_with_angle_brackets():
    """@@@"""
    stat = CSVRow(
        propertyID="<https://www.wikidata.org/wiki/Q46914185>",
    )
    stat._normalize_propid()
    assert stat._validate_propid()


def test_csvshapes_validate_property_uri_colon_only():
    """@@@"""
    stat = CSVRow(
        propertyID=":tombaker",
    )
    stat._normalize_propid()
    assert stat._validate_propid()


def test_csvshapes_validate_uristem_not():
    """@@@"""
    stat = CSVRow(
        propertyID="foobar",
    )
    stat._normalize_propid()
    assert not stat._validate_propid()
