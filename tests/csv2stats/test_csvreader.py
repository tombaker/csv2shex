"""Read CSV file and return list of rows as Python dictionaries."""

import os
import pytest
from pathlib import Path
from csv2shex.csv2stats import csvreader, Statement


def test_csvreader_with_simple_csvfile(tmp_path):
    """Simple CSV with three columns."""
    os.chdir(tmp_path)
    csvfile = Path(tmp_path).joinpath("some.csv")
    csvfile.write_text((
        "shape_id,prop_id,value_type\n"
        "@a,dct:creator,URI\n"
        "@a,dct:subject,URI\n"
        "@a,dct:date,String\n"))
    assert csvreader(csvfile) == [
        { 'shape_id': '@a', 'prop_id': 'dct:creator', 'value_type': 'URI'},
        { 'shape_id': '@a', 'prop_id': 'dct:subject', 'value_type': 'URI'},
        { 'shape_id': '@a', 'prop_id': 'dct:date', 'value_type': 'String'},
    ]


# def test_csvreader_with_complete_csvfile(tmp_path):
#     """Simple CSV with all columns."""
#     os.chdir(tmp_path)
#     csvfile = Path(tmp_path).joinpath("some.csv")
#     csvfile.write_text((
#         "shape_id,shape_label,prop_id,prop_label,mand,repeat,value_type,"
#         "value_datatype,constraint_value,constraint_type,shape_ref,annot\n"
#         "@a,Book,dct:creator,Creator,Y,N,URI,,"
#         ",,,@b,Typically the author.\n"
#         "@b,Book,dct:date,Date,Y,N,String,,"
#         "xsd:date\n,'(\d+/\d+/\d+)',Regex,"
#         "@a,Person,foaf:name,Name,Y,N,String,,,"
#         ",,,,\n"))
#     assert dict(csvreader(csvfile)) == [
#         { 
#             'shape_id': '@a', 
#             'shape_label': 'Book', 
#             'prop_id': 'dct:creator', 
#             'prop_label': 'Creator', 
#             'mand': 'Y',
#             'repeat': 'N',
#             'value_type': 'URI',
#             'value_datatype': None,
#             'constraint_value': None,
#             'constraint_type': None,
#             'shape_ref': '@b',
#             'annot': None,
#         },
#         { 
#             'shape_id': '@a', 
#             'shape_label': 'Book', 
#             'prop_id': 'dct:date', 
#             'prop_label': 'Date', 
#             'mand': 'Y',
#             'repeat': 'N',
#             'value_type': 'String',
#             'value_datatype': 'xsd:date',
#             'constraint_value': '(\d+/\d+/\d+)',
#             'constraint_type': 'Regex',
#             'shape_ref': None,
#             'annot': None,
#         },
#         { 
#             'shape_id': '@b', 
#             'shape_label': 'Person', 
#             'prop_id': 'foaf:name', 
#             'prop_label': 'Name', 
#             'mand': 'Y',
#             'repeat': 'N',
#             'value_type': 'String',
#             'value_datatype': None,
#             'constraint_value': None,
#             'constraint_type': None,
#             'shape_ref': None,
#             'annot': None,
#         },
#     ]

