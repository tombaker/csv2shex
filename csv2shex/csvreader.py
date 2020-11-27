"""Read DCAP/CSV (expand prefixes?). Write and read config file."""

from csv import DictReader
from typing import Dict, List
from pathlib import Path
from csv2shex.exceptions import CsvError
from csv2shex.csvshape import CSVSHAPE_ELEMENTS, TC_ELEMENTS
from .csvshape import CSVShape, CSVTripleConstraint, CSVSchema


def csvreader(csvfile):
    """Return list of CSVShape objects from CSV file."""
    rows = _get_rows(csvfile)
    csvshapes = _get_csvshapes(rows)
    return csvshapes


def _get_rows(csvfile):
    """Return list of row dicts from CSV file."""
    csv_dictreader = DictReader(Path(csvfile).open(newline="", encoding="utf-8-sig"))
    rows = list(csv_dictreader)
    if "propertyID" not in list(rows[0].keys()):
        raise CsvError("Valid DCAP CSV must have a 'propertyID' column.")
    return rows


def _get_csvshapes(rows=None) -> List[CSVShape]:
    """Return list of CSVShape objects from list of row dicts."""
    # /Users/tbaker/github/tombaker/csv2shex/tests/test_get_csvshapes.py

    shapes_dict: Dict[str, CSVShape] = dict()       # To index CSVShape objects.
    first_valid_row_encountered = True

    for row in rows:                                # For each row:
        if not row["propertyID"]:                   # If no propertyID in row,
            continue                                # skip and move to next row.

        if row["shapeID"]:                          # If "shapeID" specified in row,
            id_found = row["shapeID"]               # let's call it 'id_found'.
        else:                                       # Otherwise, let's make sure it
            id_found = ''                           # exists and has empty value.

        if first_valid_row_encountered:             # In first valid row encountered,
            if not id_found:                        # if no ID is found (or empty),
                id_found = ":default"               # set ID to ":default",
            shapes_dict[id_found] = CSVShape()      # and map the ID to a CSVShape,
            shapes_dict[id_found].start = True      # and that shape as "start".
            first_valid_row_encountered = False
        else:                                       # In all subsequent rows,
            if not id_found:                        # if no ID found (or empty),
                so_far = list(shapes_dict.keys())   # list shapes created so far,
                id_found = so_far[-1]               # and use the latest as ID.

        if id_found not in shapes_dict:             # On encountering a new shapeID,
            shapes_dict[id_found] = CSVShape()      # map it to new CSVShape object,
            shape = shapes_dict[id_found]           # call that object 'shape',
            for elem in CSVSHAPE_ELEMENTS:          # iterate shape-related elements,
                try:                                # to populate its attributes,
                    setattr(shape, elem, row[elem]) # with values from the row dict,
                except KeyError:                    # while any missing elements,
                    pass                            # are skipped.

        tc = CSVTripleConstraint()                  # Make triple constraint object,
        for elem in TC_ELEMENTS:                    # iterate thru relevant elements,
            try:                                    # to populate its attributes,
                setattr(tc, elem, row[elem])        # with values from the row dict,
            except KeyError:                        # while any missing elements,
                pass                                # are skipped.

        shapes_dict[id_found].tc_list.append(tc)    # Append triple constraint.

    return list(shapes_dict.values())               # Return list of shapes.

    # shape_dict = dict()
    # for csvrow_dict in rows:
    #     print(csvrow_dict["shapeID"])
    #     tripleconstraint = dict()
    #     for element in TC_ELEMENTS:
    #         tripleconstraint[element] = csvrow_dict[element]
    #     tc_list.append(tripleconstraint)

    # for csvrow_dict in rows:
    #     if csvrow_dict["shapeID"] not in dict_of_csvshapeobjs.keys():
    #         shape = CSVShape()
    #         dict_of_csvshapeobjs[csvrow_dict["shapeID"]] = shape
    #         print(dict_of_csvshapeobjs)


#     for csvrow_dict in rows:
#         if csvrow_dict["shapeID"] not in aggregator_ddict.keys():
#             shap_obj = CSVShape()
#             shap_obj.shapeID = csvrow_dict["shapeID"]
#             shap_obj.shapeLabel = csvrow_dict["shapeLabel"]
#             shap_obj.start = bool(is_first_csvrow_encountered)
#             shap_obj.tc_list = list()
#             aggregator_ddict[shap_obj.shapeID] = shap_obj
#             is_first_csvrow_encountered = False
#
#         for key in csv_model_dict["tconstraint_elements"]:
#             pvdict[key] = csvrow_dict[key]
#
#         aggregator_ddict[shap_obj.shapeID].tc_list.append(pvdict.copy())
#         pvdict.clear()
#

# def _get_csvshape_dicts_list(rows, csv_model=CSV_MODEL) -> List[dict]:
#     """Get list of csvshape dicts from list of csvrow dicts."""
#     aggregator_ddict = defaultdict(dict)
#     is_first_csvrow_encountered = True
#     pvdict = dict() # change
#     csv_model_dict = yaml.safe_load(csv_model)
#
#     for csvrow_dict in rows:
#         if csvrow_dict["shapeID"] not in aggregator_ddict.keys():
#             shap_dict = dict()
#             shap_dict["shapeID"] = csvrow_dict["shapeID"]
#             shap_dict["shapeLabel"] = csvrow_dict["shapeLabel"]
#             shap_dict["shapeClosed"] = csvrow_dict["shapeClosed"]
#             shap_dict["start"] = bool(is_first_csvrow_encountered)
#             shap_dict["tc_list"] = list()
#             aggregator_ddict[shap_dict["shapeID"]] = shap_dict
#             is_first_csvrow_encountered = False
#
#         for key in csv_model_dict["tconstraint_elements"]:
#             pvdict[key] = csvrow_dict[key]
#
#         aggregator_ddict[shap_dict["shapeID"]]["tc_list"].append(pvdict.copy())
#         pvdict.clear()

# def _get_corrected_csvrows_list(rows=None, csv_model_dict=CSV_MODEL_DICT):
#     """Turn list of dicts into list of CSVRow objects."""
#     corrected_csvrow_dicts_list = []
#     shapeids_list = []
#     first_shape_encountered = True
#     keys = csv_model_dict["shape_elements"] + csv_model_dict["tconstraint_elements"]
#     keys.remove("shapeID")
#     for row in rows:
#         if not row.get("propertyID") and row.get("shapeID"):
#             shapeids_list.append(row["shapeID"])
#             continue
#
#         stat = CSVRow()
#
#         if row.get("shapeID"):
#             stat.shapeID = row["shapeID"]
#         else:
#             if shapeids_list:
#                 stat.shapeID = shapeids_list[-1]
#             elif not shapeids_list:
#                 stat.shapeID = ":default"
#         if stat.shapeID not in shapeids_list:
#             shapeids_list.append(stat.shapeID)
#         if first_shape_encountered:
#             first_shape_encountered = False
#
#         for key in keys:
#             if key in row:
#                 setattr(stat, key, row[key])
#
#         stat.normalize()
#         stat.validate()
#         corrected_csvrow_dicts_list.append(asdict(stat))
#     return corrected_csvrow_dicts_list

