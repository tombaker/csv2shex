"""shapeClosed: default of None translates to False, variants of Yes to True."""


from csv2shex.csvrow import CSVRow


def test_csvshape_normalize_shapeclosed_to_true():
    """Normalizes "Y" to lowercase "y"."""
    stat = CSVRow(
        propertyID="wdt:P31",
        shapeClosed="Y",
    )
    stat._normalize_shapeclosed()
    assert stat.shapeClosed is True


def test_csvshape_normalize_shapeclosed_not_specified():
    """Defaults to false."""
    stat = CSVRow(
        propertyID="wdt:P31",
    )
    stat._normalize_shapeclosed()
    assert stat.shapeClosed is False
