"""Class for Python objects derived from CSV files."""


import sys
import re
import csv
from dataclasses import dataclass
from pathlib import Path
import ruamel.yaml as yaml
from .config import CSV_ELEMENTS
from .utils import is_url

# pylint: disable=no-self-use,too-many-branches,too-many-instance-attributes
# => self-use: for now...
# => too-many-branches: a matter of taste?
# => too-many-instance-attributes: disagree!

elements = yaml.safe_load(CSV_ELEMENTS)
SHAPE_ELEMENTS = elements['shape_elements']
STATEMENT_ELEMENTS = elements['statement_elements']


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
        constraint_value (str, optional):
          Etc.
        constraint_type (str, optional):
          Etc.
        shape_ref (str):
          Etc.
        annot (str):
          Etc.
    """

    start: bool = False
    shape_id: str = None
    shape_label: str = None
    prop_id: str = None
    prop_label: str = None
    mand: str = None
    repeat: str = None
    value_type: str = None
    value_datatype: str = None
    constraint_value: str = None
    constraint_type: str = None
    shape_ref: str = None
    annot: str = None

    def self_normalize(self):
        """Returns self with field values normalized."""
        self._uristem_minus_angle_brackets()

    def _uristem_minus_angle_brackets(self):
        if self.constraint_type:
            self.constraint_value = self.constraint_value.lstrip('<').rstrip('>')

    def is_valid(self):
        """Returns True if Statement instance is valid, else exits with errors."""
        self._uristem_is_used_correctly()
        # self._property_id_is_mandatory()
        # self._value_type_is_valid_type()
        return True

    def _uristem_is_used_correctly(self):
        """True if constraint type 'URIStem' is used correctly."""
        # Will have to remove the following line...
        uristem_value = self.constraint_value.lstrip('<').rstrip('>')
        if self.constraint_type == "URIStem":
            if uristem_value:
                if re.match('[A-Za-z0-9_]+:', uristem_value):
                    return True
                if is_url(uristem_value):
                    return True
                if not re.match('[A-Za-z0-9_]+:', uristem_value):
                    print(f"Warning: {repr(uristem_value)} "
                          "is not a valid URIStem.", file=sys.stderr)
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
