"""Pretty-print CSV contents to screen."""

import ruamel.yaml as yaml
from .config import CSV_MODEL


def pprint_csvshapes(csvshape_dicts_list, csv_model=CSV_MODEL, verbose=False):
    """Pretty-print CSVShape objects to console."""
    csv_model_dict = yaml.safe_load(csv_model)
    shape_elements = csv_model_dict["shape_elements"]
    statement_elements = csv_model_dict["statement_elements"]

    pprint_output = []
    pprint_output.append("DCAP")
    for csvshape_dict in csvshape_dicts_list:
        pprint_output.append("    Shape")
        for key in shape_elements:
            if not verbose and csvshape_dict[key]:
                pprint_output.append(8 * " " + key + ": " + str(csvshape_dict[key]))
            if verbose:
                pprint_output.append(8 * " " + key + ": " + str(csvshape_dict[key]))

        for stat_dict in csvshape_dict["pvdicts_list"]:
            pprint_output.append("        Statement")
            for key in statement_elements:
                if not verbose and stat_dict[key]:
                    pprint_output.append(
                        12 * " " + str(key) + ": " + str(stat_dict[key])
                    )
                if verbose:
                    pprint_output.append(
                        12 * " " + str(key) + ": " + str(stat_dict[key])
                    )

    return pprint_output
