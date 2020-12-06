"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field
from typing import List


@dataclass
class CSVTripleConstraint:
    """Instances hold TAP/CSV elements related to triple constraints."""

    # pylint: disable=too-many-instance-attributes
    # It's a dataclass, right?
    # pylint: disable=invalid-name
    # propertyID, etc, do not conform to snake-case naming style.

    propertyID: str = None
    propertyLabel: str = None
    mandatory: str = None
    repeatable: str = None
    valueNodeType: str = None
    valueDataType: str = None
    valueConstraint: str = None
    valueConstraintType: str = None
    valueShape: str = None
    note: str = None


@dataclass
class CSVShape:
    """Instances hold TAP/CSV row elements related to shapes."""

    # pylint: disable=invalid-name
    # True that propertyID, etc, do not conform to snake-case naming style.

    shapeID: str = None
    shapeLabel: str = None
    shapeClosed: str = None
    start: bool = False
    tc_list: List[CSVTripleConstraint] = field(default_factory=list)


@dataclass
class CSVSchema:
    """List of CSVShape instances"""

    csvshapes_list: List[CSVShape] = field(default_factory=list)
