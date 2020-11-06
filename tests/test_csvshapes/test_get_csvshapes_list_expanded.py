"""@@@"""

import os
import pytest
from dataclasses import asdict
import ruamel.yaml as yaml
from pathlib import Path
from csv2shex.config import get_config_settings_dict
from csv2shex.csvrows import CSVRow
from csv2shex.csvshapes import CSVShape, get_csvshapes_dict
from csv2shex.model import CSV_ELEMENTS
from csv2shex.expand import _expand_prefixes

csv_elements_dict = yaml.safe_load(CSV_ELEMENTS)
SHAPE_ELEMENTS = csv_elements_dict["shape_elements"]
STATEMENT_ELEMENTS = csv_elements_dict["statement_elements"]
SHAPE_URI_ELEMENTS = csv_elements_dict["shape_uri_elements"]
STATEMENT_URI_ELEMENTS = csv_elements_dict["statement_uri_elements"]
ALT_CONFIG_DEFAULTS = """\
prefixes:
    ":": "http://example.org/"
    "dc:": "http://purl.org/dc/terms/"
"""


def test_csvshapes_expand_prefixes_from_default_config_file(dir_with_csv2rc):
    """Get prefixes from default config file .csvrc."""
    os.chdir(Path(dir_with_csv2rc))
    assert get_config_settings_dict()["prefixes"] == {
        ":": "http://example.org/",
        "dct:": "http://purl.org/dc/terms/",
    }


def test_csvshapes_expand_prefixes_from_builtin_defaults(tmp_path):
    """Get default config settings if no default config file is found."""
    os.chdir(tmp_path)
    prefix_settings = get_config_settings_dict(config_defaults=ALT_CONFIG_DEFAULTS)[
        "prefixes"
    ]
    assert prefix_settings == {
        ":": "http://example.org/",
        "dc:": "http://purl.org/dc/terms/",
    }
    csvrows_list = [CSVRow(shapeID=":foo", propertyID="dc:creator", valueShape=":foo")]
    csvshape_dicts_list = get_csvshapes_dict(csvrows_list, expand_prefixes=True)
    assert csvshape_dicts_list
    # assert stat.shapeID == "http://example.org/"
    # assert stat.propertyID == "http://purl.org/dc/terms/creator"
    # assert stat.valueShape == "http://example.org/"


@pytest.mark.prefixes
@pytest.mark.skip
def test_get_csvshapes_dict_prefixes_expanded():
    """Turn list of CSVRow dicts into list of one CSVShape, with prefixes expanded."""
    csvrows_list = [
        CSVRow(shapeID=":a", propertyID="dct:creator", valueShape=":a"),
    ]

    expected_csvshape_dicts_list_before = [
        {
            "shapeID": ":a",
            "shapeLabel": None,
            "start": True,
            "shapeClosed": False,
            "statement_csvrows_list": [
                {
                    "propertyID": "dct:creator",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": ":a",
                    "note": None,
                }
            ],
        }
    ]

    expected_csvshape_dicts_list_expanded = [
        {
            "shapeID": "http://example.org/a",
            "shapeLabel": None,
            "start": True,
            "shapeClosed": False,
            "statement_csvrows_list": [
                {
                    "propertyID": "http://purl.org/dc/terms/creator",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": "http://example.org/a",
                    "note": None,
                }
            ],
        }
    ]
    # assert (
    #     _expand_prefixes(csvrows_list, expand_prefixes=False)
    #     == expected_csvshape_dicts_list_before
    # )
    assert (
        _expand_prefixes(csvrows_list, expand_prefixes=True)
        == expected_csvshape_dicts_list_expanded
    )
