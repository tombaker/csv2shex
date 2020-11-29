"""@@@"""


from csv2shex.csvrow import CSVRow


def test_csvshape_normalize_mandatory_to_true():
    """@@@"""
    stat = CSVRow(
        propertyID="wdt:P31",
        mandatory="Y",
    )
    stat._normalize_mandrepeat()
    assert stat.mandatory is True
    assert stat.repeatable is False


def test_csvshape_normalize_mandatory_not_specified():
    """@@@"""
    stat = CSVRow(
        propertyID="wdt:P31",
    )
    stat._normalize_mandrepeat()
    assert stat.mandatory is False
    assert stat.repeatable is False


def test_csvshape_normalize_mandatory_numeral_to_true():
    """Only variations of "yes" are True."""
    stat = CSVRow(
        propertyID="wdt:P31",
        mandatory="1",
        repeatable="0",
    )
    stat._normalize_mandrepeat()
    assert stat.mandatory is False
    assert stat.repeatable is False
