"""@@@"""


from csv2shex.mkstatements import Statement


def test_mkshapes_normalize_mandrepeat():
    """@@@"""
    stat = Statement(
        propertyID="wdt:P31",
        mand="Y",
    )
    stat._normalize_mandrepeat()
    assert stat.mand is True
    assert stat.repeat is False


def test_mkshapes_normalize_mandrepeat_not_specified():
    """@@@"""
    stat = Statement(
        propertyID="wdt:P31",
    )
    stat._normalize_mandrepeat()
    assert stat.mand is False
    assert stat.repeat is False


def test_mkshapes_normalize_mandrepeat_string_of_zero():
    """String of '0' is True!"""
    stat = Statement(
        propertyID="wdt:P31",
        mand="1",
        repeat="0",
    )
    stat._normalize_mandrepeat()
    assert stat.mand is True
    assert stat.repeat is True
