"""@@@"""

import os
import pytest
import ruamel.yaml as yaml
from pathlib import Path
from csv2shex.config import get_config_settings
from csv2shex.csvrows import CSVRow
from csv2shex.csvshapes import CSVShape, list_csvshapeobjs
from csv2shex.config import CSV_ELEMENTS

elements = yaml.safe_load(CSV_ELEMENTS)
URI_ELEMENTS = elements["uri_elements"]

ALT_CONFIG_DEFAULTS = """\
prefixes:
    ":": "http://example.org/"
    "dc:": "http://purl.org/dc/terms/"
"""


def test_csvshapes_expand_prefixes_from_default_config_file(dir_with_csv2rc):
    """Get prefixes from default config file .csvrc."""
    os.chdir(Path(dir_with_csv2rc))
    assert get_config_settings()["prefixes"] == {
        ":": "http://example.org/",
        "dct:": "http://purl.org/dc/terms/",
    }


def test_csvshapes_expand_prefixes_from_builtin_defaults(tmp_path):
    """Get default config settings if no default config file is found."""
    os.chdir(tmp_path)
    prefix_settings = get_config_settings(config_defaults=ALT_CONFIG_DEFAULTS)[
        "prefixes"
    ]
    assert prefix_settings == {
        ":": "http://example.org/",
        "dc:": "http://purl.org/dc/terms/",
    }
    csvrows_list = [CSVRow(shapeID=":foo", propertyID="dc:creator", valueShape=":foo")]
    csvshapes_list = list_csvshapeobjs(csvrows_list, expand_prefixes=True)
    assert csvshapes_list
    # assert stat.shapeID == "http://example.org/"
    # assert stat.propertyID == "http://purl.org/dc/terms/creator"
    # assert stat.valueShape == "http://example.org/"


@pytest.mark.prefixes
@pytest.mark.skip
def test_list_csvshapeobjs_prefixes_expanded():
    """Turn list of CSVRow objects into list of one CSVShape with prefixes expanded."""
    csvrows_list = [
        CSVRow(shapeID=":a", propertyID="dct:creator", valueShape=":a"),
    ]

    expected_csvshapes_list = [
        CSVShape(
            start=True,
            shapeID="http://example.org/a",
            shapeLabel=None,
            statement_csvrows_list=[
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
                },
            ],
        )
    ]
    assert (
        list_csvshapeobjs(csvrows_list, expand_prefixes=True) == expected_csvshapes_list
    )
