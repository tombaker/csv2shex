"""Class for Python objects derived from CSV files."""

import re
import ruamel.yaml as yaml
from .config import CONFIG_DEFAULTS
from .model import CSV_MODEL

# pylint: disable=unused-argument
# pylint: disable=unused-variable
# pylint: disable=undefined-variable

PREFIXES_DICT = yaml.safe_load(CONFIG_DEFAULTS)["prefixes"]
CSV_MODEL_DICT = yaml.safe_load(CSV_MODEL)


def _expand_prefixes(
    csvshape_dicts_list, csv_model_dict=None, prefixes_dict=PREFIXES_DICT
):
    prefixed_uri_regex = re.compile("([a-z0-9])*:([a-zA-Z0-9])*")
    # prefixes_dict = config_settings_dict["prefixes"]
    prefixes_dict[":"] = prefixes_dict[None]
    # >>> prefixes_dict
    # {':': 'http://example.org/', 'dct:': 'http://purl.org/dc/terms/'}

    # "dct:date".replace("dct:", config_settings["prefixes"]["dct:"])
    for shape in csvshape_dicts_list:
        for element in csv_model_dict["shape_uri_elements"]:
            print(shape[element])
            shape[element] = ":bar"
            print(shape[element])
        for element in csv_model_dict["statement_uri_elements"]:
            pass
            # for csvrow in element['statement_csvrows_list']:

    csvshape_dicts_list_expanded = 1
    return csvshape_dicts_list_expanded
