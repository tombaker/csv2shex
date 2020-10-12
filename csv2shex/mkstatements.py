"""Class for Python objects derived from CSV files."""


import re
import sys
from dataclasses import dataclass
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

        shapeID (str, assigned if not provided):
          Identifier of the shape to which the statement
          (property-value pair) belongs.
          If no shape identifier is provided in the CSV,
          a default identifier is assigned.
        shapeLabel (str, optional):
          Human-readable label for the shape. Default: None.
        start (bool, assigned):
          If True, shape is a "start" shape. Default: False.
        propertyID (str, mandatory):
          Identifier of the property (of the property-value
          pair) as a URI string or prefixed URI string.
          Default: None.
        propertyLabel (str, optional):
          Human-readable label for the property. Default: None.
        mandatory (str, optional):
          If True, use of the property is mandatory in the
          context of the shape. Values interpreted as True
          include `Y`, `y`, `Yes`, and `yes`. Default: False.
        repeatable (str, optional):
          If True, property may be used multiple times in the
          context of the shape. Values interpreted as True
          include `Y`, `y`, `Yes`, and `yes`. Default: False.
        valueNodeType (str, optional):
          Value of the property-value pair is one of the type
          `URI`, `BNode`, `Literal`, or `Non-Literal`.
          Default: None. Value type `IRI` is normalized to `URI`.
        valueDataType (str, optional):
          The specific datatype of the literal value,
          identified by a URI string or prefixed URI string,
          typically from the XML Schema namespace.
        valueConstraint (str, optional):
          Etc.
        valueConstraintType (str, optional):
          Etc.
        value_shape (str, optional):
          Etc.
        note (str, optional):
          Etc.
    """

    start: bool = False
    shapeID: str = None
    shapeLabel: str = None
    propertyID: str = None
    propertyLabel: str = None
    mandatory: bool = False
    repeatable: bool = False
    valueNodeType: str = None
    valueDataType: str = None
    valueConstraint: str = None
    valueConstraintType: str = None
    value_shape: str = None
    note: str = None

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
        """Elements 'mandatory' or 'repeatable' are True if any value provided."""
        if self.mandatory:
            self.mandatory = True
        if self.repeatable:
            self.repeatable = True

    def _normalize_propid(self):
        """Normalize URIs by stripping angle brackets."""
        propid = self.propertyID
        self.propertyID = propid.lstrip("<").rstrip(">")
        return self

    def _normalize_uristem(self):
        """Normalize URI stems as constraint values."""
        if self.valueConstraintType == "UriStem":
            if self.valueConstraint:
                uristem = self.valueConstraint
                self.valueConstraint = uristem.lstrip("<").rstrip(">")
        return self

    def _normalize_uripicklist(self):
        """@@@"""
        if self.valueConstraintType == "UriPicklist":
            self.valueConstraint = self.valueConstraint.split()
        return self

    def _normalize_litpicklist(self):
        """@@@"""
        if self.valueConstraintType == "LitPicklist":
            self.valueConstraint = self.valueConstraint.split()
        return self

    def _normalize_regex(self):
        """Regex must be a valid (Python) regex."""
        if self.valueConstraintType == "Regex":
            if not self.valueNodeType:
                self.valueNodeType = "Literal"
            if self.valueConstraint:
                try:
                    self.valueConstraint = re.compile(self.valueConstraint)
                except (re.error, TypeError):
                    print(
                        f"{repr(self.valueConstraint)} is not "
                        "a valid (Python) regular expression.",
                        file=sys.stderr,
                    )
                    self.valueConstraint = None

    def _normalize_datatype(self):
        """Datatype must be a valid URI."""
        if self.valueConstraintType == "Datatype":
            if not self.valueNodeType:
                self.valueNodeType = "Literal"
            if self.valueConstraint:
                if not is_valid_uri_or_prefixed_uri(self.valueConstraint):
                    self.valueConstraint = None

    def _normalize_valueuri(self):
        """Normalize value URIs by stripping angle brackets."""
        if self.valueNodeType == "URI":
            if self.valueConstraint is not None:
                uri_as_value = self.valueConstraint
                self.valueConstraint = uri_as_value.lstrip("<").rstrip(">")
        return self

    def _validate_propid(self):
        """True if property ID is a URI or prefixed URI."""
        # propid is mandatory. If this returns False, exit with error?
        if not is_valid_uri_or_prefixed_uri(self.propertyID):
            return False
        return True

    def _validate_uripicklist(self):
        """True if all members of UriPicklist are URIs."""
        if self.valueConstraintType == "UriPicklist":
            return all([is_uri(item) for item in self.valueConstraint])
        return True

    def _validate_litpicklist(self):
        """True if all members of LitPicklist are strings."""
        if self.valueConstraintType == "LitPicklist":
            return all([isinstance(item, str) for item in self.valueConstraint])
        return True

    def _validate_uristem(self):
        """True if constraint value for constraint type UriStem is a valid URI."""
        if self.valueConstraintType == "UriStem":
            uristem_value = self.valueConstraint
            if uristem_value:
                if not is_valid_uri_or_prefixed_uri(uristem_value):
                    return False
        return True

    def _validate_valueuri(self):
        """True if constraint value for value type URI is a valid URI."""
        if self.valueNodeType == "URI":
            uri_value = self.valueConstraint
            if uri_value:
                if not is_valid_uri_or_prefixed_uri(uri_value):
                    return False
        return True


def list_statements(csvrow_dicts_list_normalized=None):
    """Return list of Statement objects from list of dicts ("CSV rows")."""
    statements_list = []
    shapeIDs = []
    first_shape_encountered = True
    keys = SHAPE_ELEMENTS + STATEMENT_ELEMENTS
    keys.remove("shapeID")
    for row in csvrow_dicts_list_normalized:
        if not row.get("propertyID") and row.get("shapeID"):
            shapeIDs.append(row["shapeID"])
            continue

        stat = Statement()

        if row.get("shapeID"):
            stat.shapeID = row["shapeID"]
        else:
            if shapeIDs:
                stat.shapeID = shapeIDs[-1]
            elif not shapeIDs:
                stat.shapeID = "@default"
        if stat.shapeID not in shapeIDs:
            shapeIDs.append(stat.shapeID)
        if first_shape_encountered:
            first_shape = stat.shapeID
            first_shape_encountered = False
        if stat.shapeID == first_shape:
            stat.start = True

        for key in keys:
            if key in row:
                setattr(stat, key, row[key])

        statements_list.append(stat)
    return statements_list
