"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field, asdict
from collections import defaultdict
from typing import List
import ruamel.yaml as yaml
from .config import CSV_MODEL

CSV_MODEL_DICT = yaml.safe_load(CSV_MODEL)


@dataclass
class Tconstraint:
    """Holds state for CSV triple constraint elements."""


@dataclass
class CSVShape:
    """Holds state and self-validation methods for a CSVShape."""

    shapeID: str = None
    shapeLabel: str = None
    shapeClosed: str = None
    start: bool = False
    pvdicts_list: List[Tconstraint] = field(default_factory=list)

