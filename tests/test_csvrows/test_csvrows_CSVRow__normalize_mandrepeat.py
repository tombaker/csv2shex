"""@@@"""


from csv2shex.csvrow import CSVRow


def test_csvshape_normalize_mandrepeat():
    """@@@"""
    stat = CSVRow(
        propertyID="wdt:P31",
        mandatory="Y",
    )
    stat._normalize_mandrepeat()
    assert stat.mandatory is True
    assert stat.repeatable is False


def test_csvshape_normalize_mandrepeat_not_specified():
    """@@@"""
    stat = CSVRow(
        propertyID="wdt:P31",
    )
    stat._normalize_mandrepeat()
    assert stat.mandatory is False
    assert stat.repeatable is False


def test_csvshape_normalize_mandrepeat_string_of_zero():
    """String of '0' is True!"""
    stat = CSVRow(
        propertyID="wdt:P31",
        mandatory="1",
        repeatable="0",
    )
    stat._normalize_mandrepeat()
    assert stat.mandatory is True
    assert stat.repeatable is True
