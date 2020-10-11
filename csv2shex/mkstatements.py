"""Class for Python objects derived from CSV files."""


import re
import sys
import csv
from dataclasses import dataclass
from pathlib import Path
import ruamel.yaml as yaml
from .config import CSV_ELEMENTS
from .utils import is_uri, is_valid_uri_or_prefixed_uri

# pylint: disable=no-self-use,too-many-branches,too-many-instance-attributes
# => self-use: for now...
# => too-many-branches: a matter of taste?
# => too-many-instance-attributes: disagree!

elements = yaml.safe_load(CSV_ELEMENTS)
SHAPE_ELEMENTS = elements["shape_elements"]
STATEMENT_ELEMENTS = elements["statement_elements"]


@dataclass
class Statement:
    """Holds state and self-validation methods for a statement.

    Dataclass fields:

        shape_id (str, assigned if not provided):
          Identifier of the shape to which the statement
          (property-value pair) belongs.
          If no shape identifier is provided in the CSV,
          a default identifier is assigned.
        shape_label (str, optional):
          Human-readable label for the shape. Default: None.
        start (bool, assigned):
          If True, shape is a "start" shape. Default: False.
        prop_id (str, mandatory):
          Identifier of the property (of the property-value
          pair) as a URI string or prefixed URI string.
          Default: None.
        prop_label (str, optional):
          Human-readable label for the property. Default: None.
        mand (str, optional):
          If True, use of the property is mandatory in the
          context of the shape. Values interpreted as True
          include `Y`, `y`, `Yes`, and `yes`. Default: False.
        repeat (str, optional):
          If True, property may be used multiple times in the
          context of the shape. Values interpreted as True
          include `Y`, `y`, `Yes`, and `yes`. Default: False.
        value_type (str, optional):
          Value of the property-value pair is one of the type
          `URI`, `BNode`, `Literal`, or `Non-Literal`.
          Default: None. Value type `IRI` is normalized to `URI`.
        value_datatype (str, optional):
          The specific datatype of the literal value,
          identified by a URI string or prefixed URI string,
          typically from the XML Schema namespace.
        value_constraint (str, optional):
          Etc.
        constraint_type (str, optional):
          Etc.
        shape_ref (str, optional):
          Etc.
        annot (str, optional):
          Etc.
    """

    start: bool = False
    shape_id: str = None
    shape_label: str = None
    prop_id: str = None
    prop_label: str = None
    mand: bool = False
    repeat: bool = False
    value_type: str = None
    value_datatype: str = None
    value_constraint: str = None
    constraint_type: str = None
    shape_ref: str = None
    annot: str = None

    def normalize(self):
        """Normalize specific elements."""
        self._normalize_litpicklist()
        self._normalize_mandrepeat()
        self._normalize_propid()
        self._normalize_regex()
        self._normalize_datatype()
        self._normalize_uripicklist()
        self._normalize_uristem()
        self._normalize_valueuri()
        # self._normalize_langtag()
        # self._normalize_langtag_picklist()

    def validate(self):
        """True if Statement instance is valid, else exit with errors."""
        self._validate_litpicklist()
        self._validate_propid()
        self._validate_uripicklist()
        self._validate_uristem()
        self._validate_valueuri()
        return True

    def _normalize_mandrepeat(self):
        """Elements 'mand' or 'repeat' are True if any value provided."""
        if self.mand:
            self.mand = True
        if self.repeat:
            self.repeat = True

    def _normalize_propid(self):
        """Normalize URIs by stripping angle brackets."""
        propid = self.prop_id
        self.prop_id = propid.lstrip("<").rstrip(">")
        return self

    def _normalize_uristem(self):
        """Normalize URI stems as constraint values."""
        if self.constraint_type == "UriStem":
            if self.value_constraint:
                uristem = self.value_constraint
                self.value_constraint = uristem.lstrip("<").rstrip(">")
        return self

    def _normalize_uripicklist(self):
        """@@@"""
        if self.constraint_type == "UriPicklist":
            self.value_constraint = self.value_constraint.split()
        return self

    def _normalize_litpicklist(self):
        """@@@"""
        if self.constraint_type == "LitPicklist":
            self.value_constraint = self.value_constraint.split()
        return self

    def _normalize_regex(self):
        """Regex must be a valid (Python) regex."""
        if self.constraint_type == "Regex":
            if not self.value_type:
                self.value_type = "Literal"
            if self.value_constraint:
                try:
                    self.value_constraint = re.compile(self.value_constraint)
                except (re.error, TypeError):
                    print(
                        f"{repr(self.value_constraint)} is not "
                        "a valid (Python) regular expression.",
                        file=sys.stderr,
                    )
                    self.value_constraint = None

    def _normalize_datatype(self):
        """Datatype must be a valid URI."""
        if self.constraint_type == "Datatype":
            if not self.value_type:
                self.value_type = "Literal"
            if self.value_constraint:
                if not is_valid_uri_or_prefixed_uri(self.value_constraint):
                    self.value_constraint = None

    def _normalize_valueuri(self):
        """Normalize value URIs by stripping angle brackets."""
        if self.value_type == "URI":
            if self.value_constraint is not None:
                uri_as_value = self.value_constraint
                self.value_constraint = uri_as_value.lstrip("<").rstrip(">")
        return self

    def _validate_propid(self):
        """True if property ID is a URI or prefixed URI."""
        # propid is mandatory. If this returns False, exit with error?
        if not is_valid_uri_or_prefixed_uri(self.prop_id):
            return False
        return True

    def _validate_uripicklist(self):
        """True if all members of UriPicklist are URIs."""
        if self.constraint_type == "UriPicklist":
            return all([is_uri(item) for item in self.value_constraint])
        return True

    def _validate_litpicklist(self):
        """True if all members of LitPicklist are strings."""
        if self.constraint_type == "LitPicklist":
            return all([isinstance(item, str) for item in self.value_constraint])
        return True

    def _validate_uristem(self):
        """True if constraint value for constraint type UriStem is a valid URI."""
        if self.constraint_type == "UriStem":
            uristem_value = self.value_constraint
            if uristem_value:
                if not is_valid_uri_or_prefixed_uri(uristem_value):
                    return False
        return True

    def _validate_valueuri(self):
        """True if constraint value for value type URI is a valid URI."""
        if self.value_type == "URI":
            uri_value = self.value_constraint
            if uri_value:
                if not is_valid_uri_or_prefixed_uri(uri_value):
                    return False
        return True


def csvreader(csvfile):
    """Read CSV file and return list of dicts, one dict per CSV row."""
    rows_odict = csv.DictReader(Path(csvfile).open(newline="", encoding="utf-8-sig"))
    rows = [dict(r) for r in rows_odict]
    return rows


def list_statements(csvrow_list=None):
    """Return list of Statement objects from list of dicts ("CSV rows")."""
    statements_list = []
    shape_ids = []
    first_shape_encountered = True
    keys = SHAPE_ELEMENTS + STATEMENT_ELEMENTS
    keys.remove("shape_id")
    for row in csvrow_list:
        if not row.get("prop_id") and row.get("shape_id"):
            shape_ids.append(row["shape_id"])
            continue

        stat = Statement()

        if row.get("shape_id"):
            stat.shape_id = row["shape_id"]
        else:
            if shape_ids:
                stat.shape_id = shape_ids[-1]
            elif not shape_ids:
                stat.shape_id = "@default"
        if stat.shape_id not in shape_ids:
            shape_ids.append(stat.shape_id)
        if first_shape_encountered:
            first_shape = stat.shape_id
            first_shape_encountered = False
        if stat.shape_id == first_shape:
            stat.start = True

        for key in keys:
            if key in row:
                setattr(stat, key, row[key])

        statements_list.append(stat)
    return statements_list
