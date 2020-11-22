"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field
from typing import List
import ruamel.yaml as yaml
from .config import CSV_MODEL


@dataclass
class CSVTripleConstraint:
    """Elements, from a DC TAP CSV row, forming a triple constraint."""

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
    """Elements, from a DC TAP CSV row, forming a shape."""

    shapeID: str = None
    shapeLabel: str = None
    shapeClosed: str = None
    start: bool = False
    tripleconstraints_list: List[CSVTripleConstraint] = field(default_factory=list)
