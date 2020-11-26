"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field, asdict
from typing import List


@dataclass
class CSVTripleConstraint:
    """Instances hold TAP/CSV elements that form a triple constraint."""

    propertyID: str = None
    valueConstraint: str = None
    valueShape: str = None
    # propertyLabel: str = None
    # mandatory: str = None
    # repeatable: str = None
    # valueNodeType: str = None
    # valueDataType: str = None
    # valueConstraintType: str = None
    # note: str = None


@dataclass
class CSVShape:
    """Instances hold TAP/CSV row elements that form a shap."""

    shapeID: str = None
    # shapeLabel: str = None
    # shapeClosed: str = None
    start: bool = False
    tripleconstraints_list: List[CSVTripleConstraint] = field(default_factory=list)


@dataclass
class CSVSchema:
    """List of CSVShape instances??"""


csvshape_keys = list(asdict(CSVShape()).keys())
csvshape_keys.remove('tripleconstraints_list')
CSVSHAPE_ELEMENTS = csvshape_keys
CSVTRIPLECONSTRAINT_ELEMENTS = list(asdict(CSVTripleConstraint()).keys())
