"""Check CSV file structure for anomalies"""


from csv2shex.csvrows import CSVRow


def test_csvshapes_validate_uristem_prefixed():
    """@@@"""
    statement = CSVRow(
        shapeID="@default",
        propertyID="wdt:P31",
        valueConstraint="wd:",
        valueConstraintType="UriStem",
    )
    assert statement._validate_uristem()


def test_csvshapes_validate_uristem_normal_uri():
    """@@@"""
    statement = CSVRow(
        shapeID="@default",
        propertyID="wdt:P31",
        valueConstraint="http://www.gmd.de/",
        valueConstraintType="UriStem",
    )
    assert statement._validate_uristem()


def test_csvshapes_validate_uristem_with_angle_brackets():
    """@@@"""
    statement = CSVRow(
        shapeID="@default",
        propertyID="wdt:P31",
        valueConstraint="<http://www.gmd.de/>",
        valueConstraintType="UriStem",
    )
    statement._normalize_uristem()
    assert statement._validate_uristem()


def test_csvshapes_validate_uristem_colon_only():
    """@@@"""
    statement = CSVRow(
        shapeID="@default",
        propertyID="wdt:P31",
        valueConstraint=":",
        valueConstraintType="UriStem",
    )
    statement._normalize_uristem()
    assert statement._validate_uristem()


def test_csvshapes_validate_uristem_not():
    """@@@"""
    statement = CSVRow(
        shapeID="@default",
        propertyID="wdt:P31",
        valueConstraint="foobar",
        valueConstraintType="UriStem",
    )
    statement._normalize_uristem()
    assert not statement._validate_uristem()
