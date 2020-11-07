"""@@@"""


from csv2shex.csvrow import CSVRow


def test_csvshapes_normalize_litpicklist():
    """@@@"""
    stat = CSVRow(
        propertyID="wdt:P31",
        valueConstraint="red green yellow",
        valueConstraintType="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat.valueConstraint == ["red", "green", "yellow"]


def test_csvshapes_normalize_litpicklist_just_one_item():
    """@@@"""
    stat = CSVRow(
        propertyID="wdt:P31",
        valueConstraint="red",
        valueConstraintType="LitPicklist",
    )
    stat._normalize_litpicklist()
    assert stat.valueConstraint == ["red"]
