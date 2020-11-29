"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field
from typing import List


@dataclass
class CSVTripleConstraint:
    """Instances hold TAP/CSV elements related to triple constraints."""

    # pylint: disable=too-many-instance-attributes
    # It's a dataclass, right?

    propertyID: str = ""
    valueConstraint: str = ""
    valueShape: str = ""
    # propertyLabel: str = None
    mandatory: str = ""
    repeatable: str = ""
    valueNodeType: str = None
    valueDataType: str = None
    valueConstraintType: str = None
    # note: str = None


@dataclass
class CSVShape:
    """Instances hold TAP/CSV row elements related to shapes."""

    shapeID: str = ""
    # shapeLabel: str = None
    # shapeClosed: str = None
    start: bool = False
    tc_list: List[CSVTripleConstraint] = field(default_factory=list)


@dataclass
class CSVSchema:
    """List of CSVShape instances??"""
