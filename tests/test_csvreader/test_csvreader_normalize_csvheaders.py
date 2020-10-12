"""Normalize variant CSV headers to just one form."""

# from pathlib import Path
import ruamel.yaml as yaml
from textwrap import dedent
# from csv2shex.csvreader import normalize_csvheaders


def test_normalize_csvheaders_yaml_format_for_variants():
    """Just tests basic YAML format."""
    csv_elements_indented = """\
    shape_elements:
    - shapeid:
      - Shape Identifier
      - Shape ID
    """
    csv_elements = dedent(csv_elements_indented)
    input = yaml.safe_load(csv_elements)
    assert input == {
        "shape_elements": [{"shapeid": ["Shape Identifier", "Shape ID"]}]
    }


def test_normalize_csvheaders_normalize_yaml_format_for_variants():
    """Normalizes 'Shape Identifier' and 'Shape ID' to 'shapeid'."""
    csv_elements_indented = """\
    shape_elements:
    - shapeid:
      - Shape Identifier
      - Shape ID
    """
    csv_elements = dedent(csv_elements_indented)
    input = yaml.safe_load(csv_elements)
    assert input == {"shape_elements": [{"shapeid": ["Shape Identifier", "Shape ID"]}]}
