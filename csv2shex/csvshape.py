"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field, asdict
from collections import defaultdict
from typing import List
import ruamel.yaml as yaml
from .config import CSV_MODEL

CSV_MODEL_DICT = yaml.safe_load(CSV_MODEL)


@dataclass
class CSVTripleConstraint:
    """Elements, from a DC TAP CSV row, forming a triple constraint."""


@dataclass
class CSVShape:
    """Elements, from a DC TAP CSV row, forming a shape."""

    shapeID: str = None
    shapeLabel: str = None
    shapeClosed: str = None
    start: bool = False
    tripleconstraints_list: List[CSVTripleConstraint] = field(default_factory=list)

