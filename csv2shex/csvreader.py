"""Read DCAP/CSV (expand prefixes?). Write and read config file."""

from csv import DictReader
from pathlib import Path
from csv2shex.exceptions import CsvError
# from .csvshape import CSVShape, CSVTripleConstraint, CSVSchema


def csvreader(csvfile):
    """Read CSV file and return list of CSV shapes, one dict per CSV shape."""
    rows = _get_rows(csvfile)
    csvshapes = _get_csvshapes(rows)
    return csvshapes


def _get_rows(csvfile):
    """Return list of CSV rows (as dicts) from CSV file."""
    csv_dictreader = DictReader(Path(csvfile).open(newline="", encoding="utf-8-sig"))
    rows = list(csv_dictreader)
    if "propertyID" not in list(rows[0].keys()):
        raise CsvError("Valid DCAP CSV must have a 'propertyID' column.")
    return rows


def _get_csvshapes(rows=None):
    """Return list of CSVShape instances from list of CSV rows (as dicts)."""
    # /Users/tbaker/github/tombaker/csv2shex/csv2shex/test_get_csvshapes.py

    return rows

    # dict_of_csvshapeobjs = dict()
    # tripleconstraints_list = list()
    # shape_dict = dict()
    # for csvrow_dict in rows:
    #     print(csvrow_dict["shapeID"])
    #     tripleconstraint = dict()
    #     for element in CSVTRIPLECONSTRAINT_ELEMENTS:
    #         tripleconstraint[element] = csvrow_dict[element]
    #     tripleconstraints_list.append(tripleconstraint)

    # dict_of_csvshapeobjs = dict()
    # for csvrow_dict in rows:
    #     if csvrow_dict["shapeID"] not in dict_of_csvshapeobjs.keys():
    #         shape = CSVShape()
    #         dict_of_csvshapeobjs[csvrow_dict["shapeID"]] = shape
    #         print(dict_of_csvshapeobjs)


# def _get_csvshape_dicts_list(rows, csv_model=CSV_MODEL) -> List[dict]:
#     """Get list of csvshape dicts from list of csvrow dicts."""
#     aggregator_ddict = defaultdict(dict)
#     is_first_csvrow_encountered = True
#     pvdict = dict()
#     csv_model_dict = yaml.safe_load(csv_model)
#
#     for csvrow_dict in rows:
#         if csvrow_dict["shapeID"] not in aggregator_ddict.keys():
#             shap_obj = CSVShape()
#             shap_obj.shapeID = csvrow_dict["shapeID"]
#             shap_obj.shapeLabel = csvrow_dict["shapeLabel"]
#             shap_obj.start = bool(is_first_csvrow_encountered)
#             shap_obj.tripleconstraints_list = list()
#             aggregator_ddict[shap_obj.shapeID] = shap_obj
#             is_first_csvrow_encountered = False
#
#         for key in csv_model_dict["tconstraint_elements"]:
#             pvdict[key] = csvrow_dict[key]
#
#         aggregator_ddict[shap_obj.shapeID].tripleconstraints_list.append(pvdict.copy())
#         pvdict.clear()
#
#     csvshape_dicts_list = []
#     for key in aggregator_ddict.keys():
#         csvshape_dict = aggregator_ddict[key]
#         csvshape_dicts_list.append(csvshape_dict)
#
#     return csvshape_dicts_list
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
#             shap_dict["tripleconstraints_list"] = list()
#             aggregator_ddict[shap_dict["shapeID"]] = shap_dict
#             is_first_csvrow_encountered = False
#
#         for key in csv_model_dict["tconstraint_elements"]:
#             pvdict[key] = csvrow_dict[key]
#
#         aggregator_ddict[shap_dict["shapeID"]]["tripleconstraints_list"].append(pvdict.copy())
#         pvdict.clear()
#
#     csvshape_dicts_list = []
#     for key in aggregator_ddict.keys():
#         csvshape_dict = aggregator_ddict[key]
#         csvshape_dicts_list.append(csvshape_dict)
#
#     return csvshape_dicts_list


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
