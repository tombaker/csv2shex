"""Class for Python objects derived from CSV files."""


import re
import sys
from dataclasses import dataclass
import ruamel.yaml as yaml
from .defaults import CSV_MODEL
from .utils import is_uri, is_valid_uri_or_prefixed_uri

csv_model = yaml.safe_load(CSV_MODEL)
SHAPE_ELEMENTS = csv_model["shape_elements"]
STATEMENT_ELEMENTS = csv_model["statement_elements"]

# pylint: disable=no-self-use,too-many-branches,too-many-instance-attributes
# => self-use: for now...
# => too-many-branches: a matter of taste?
# => too-many-instance-attributes: disagree!


@dataclass
class CSVRow:
    """Holds state and self-validation methods for a property-value pair.

    Dataclass fields:

        shapeID (str, assigned default if not provided):
          Identifier of shape to which statement
          (property-value pair) belongs.

        shapeLabel (str, optional):
          Human-readable label for shape. Default: None.

        shapeClosed (str, optional):
          If True, shape requires listed statements and no more.

        start (str, optional):
          If True, shape is considered as "start shape".

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
          typically from the XML Schema namespace. Default: None.

        valueConstraint (str, optional):
          Etc.
          Default: None.

        valueConstraintType (str, optional):
          Etc.
          Default: None.

        valueShape (str, optional):
          Etc.
          Default: None.

        note (str, optional):
          Etc.
          Default: None.
    """

    shapeID: str = None
    shapeLabel: str = None
    shapeClosed: bool = False
    start: bool = False
    propertyID: str = None
    propertyLabel: str = None
    mandatory: bool = False
    repeatable: bool = False
    valueNodeType: str = None
    valueDataType: str = None
    valueConstraint: str = None
    valueConstraintType: str = None
    valueShape: str = None
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
        """True if CSVRow instance is valid, else exit with errors."""
        self._validate_litpicklist()
        self._validate_propid()
        self._validate_uripicklist()
        self._validate_uristem()
        self._validate_valueuri()
        return True

    def _normalize_mandrepeat(self):
        """@@@ Elements 'mandatory' or 'repeatable' are True if any value provided."""
        if self.mandatory:
            self.mandatory = True
        if self.repeatable:
            self.repeatable = True

    def _normalize_propid(self):
        """Normalize URIs by stripping angle brackets."""
        propid = self.propertyID
        if propid:
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


def get_csvrowobjs_list(csvrow_dicts_list=None):
    """Turn list of dicts into list of CSVRow objects."""
    csvrows_list = []
    shapeids_list = []
    first_shape_encountered = True
    keys = SHAPE_ELEMENTS + STATEMENT_ELEMENTS
    keys.remove("shapeID")
    for row in csvrow_dicts_list:
        if not row.get("propertyID") and row.get("shapeID"):
            shapeids_list.append(row["shapeID"])
            continue

        stat = CSVRow()

        if row.get("shapeID"):
            stat.shapeID = row["shapeID"]
        else:
            if shapeids_list:
                stat.shapeID = shapeids_list[-1]
            elif not shapeids_list:
                stat.shapeID = ":default"
        if stat.shapeID not in shapeids_list:
            shapeids_list.append(stat.shapeID)
        if first_shape_encountered:
            first_shape_encountered = False

        for key in keys:
            if key in row:
                setattr(stat, key, row[key])

        csvrows_list.append(stat)
    return csvrows_list


#        # Checking for presence of propertyID will ensure that blank rows are ignored.
#        if row.get("propertyID"):
#            if first_statement_encountered:
#                # Assign row value for shapeID, if available, to stat.shapeID.
#                if row.get("shapeID"):
#                    stat.shapeID = row["shapeID"]
#                else:
#                    stat.shapeID = ":default"
#                shapeids_list.append(stat.shapeID)
#                first_statement_encountered = False
#                first_shape_encountered = False
#            # If shapeID is None, assign value most recently added to shapeids_list.
#            if not row.get("shapeID"):
#                stat.shapeID = shapeids_list[-1]
