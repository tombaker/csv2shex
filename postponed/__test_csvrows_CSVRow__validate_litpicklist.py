"""@@@"""


from csv2shex.csvrow import CSVRow


def test_csvshape_validate_litpicklist():
    """@@@"""
    stat = CSVRow(
        propertyID="wdt:P31",
        valueConstraint="red green yellow",
        valueConstraintType="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat._validate_litpicklist()


def test_csvshape_validate_litpicklist_just_one_item():
    """@@@"""
    stat = CSVRow(
        shapeID=":default",
        propertyID="wdt:P31",
        valueConstraint="red",
        valueConstraintType="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat._validate_litpicklist()
