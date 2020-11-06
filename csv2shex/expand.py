"""Class for Python objects derived from CSV files."""

import re
from .model import CSV_ELEMENTS


def _expand_prefixes(csvshape_dicts_list, csv_elements=CSV_ELEMENTS, expand_prefixes=False):
    prefixed_uri_regex = re.compile("([a-z0-9])*:([a-zA-Z0-9])*")
    prefixes[":"] = prefixes[None]
    if expand_prefixes:
        prefixes_dict = config_settings_dict["prefixes"]
        # >>> prefixes_dict
        # {':': 'http://example.org/', 'dct:': 'http://purl.org/dc/terms/'}
        "dct:date".replace("dct:", config_settings['prefixes']['dct:'])
        for shape in csvshape_dicts_list:
            for element in csv_elements_dict["shape_uri_elements"]:
                print(shape[element])
                shape[element] = ":bar"
                print(shape[element])
            for element in csv_elements_dict["statement_uri_elements"]:
                pass
                # for csvrow in element['statement_csvrows_list']:
    return csvshape_dicts_list_expanded
