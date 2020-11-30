"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field
from typing import List


@dataclass
class CSVTripleConstraint:
    """Instances hold TAP/CSV elements related to triple constraints."""

    # pylint: disable=too-many-instance-attributes
    # It's a dataclass, right?
    # pylint: disable=invalid-name
    # True that propertyID, etc, do not conform to snake-case naming style.

    propertyID: str = ""
    propertyLabel: str = ""
    mandatory: str = ""
    repeatable: str = ""
    valueNodeType: str = ""
    valueDataType: str = ""
    valueConstraint: str = ""
    valueConstraintType: str = ""
    valueShape: str = ""
    note: str = ""


@dataclass
class CSVShape:
    """Instances hold TAP/CSV row elements related to shapes."""

    # pylint: disable=invalid-name
    # True that propertyID, etc, do not conform to snake-case naming style.

    shapeID: str = ""
    # shapeLabel: str = None
    # shapeClosed: str = None
    start: bool = False
    tc_list: List[CSVTripleConstraint] = field(default_factory=list)


@dataclass
class CSVSchema:
    """List of CSVShape instances??"""
