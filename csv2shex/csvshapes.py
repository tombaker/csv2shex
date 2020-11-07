"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field
from typing import List
from .csvrows import CSVRow


@dataclass
class CSVShape:
    """Holds state and self-validation methods for a CSVShape."""

    shapeID: str = None
    shapeLabel: str = None
    start: bool = False
    shapeClosed: bool = False
    statement_csvrows_list: List[CSVRow] = field(default_factory=list)
