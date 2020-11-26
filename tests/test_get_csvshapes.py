"""Read CSV file and return list of rows as Python dictionaries."""
# /Users/tbaker/github/tombaker/csv2shex/csv2shex/csvreader.py

import pytest
from csv2shex.csvreader import _get_csvshapes
from csv2shex.csvshape import CSVShape
#     CSVTripleConstraint,
#     CSVSchema,
#     CSVSHAPE_ELEMENTS,
#     CSVTRIPLECONSTRAINT_ELEMENTS,
# )


@pytest.mark.skip
def test_get_csvshape_list():
    """Minimal CSV with three columns."""
    rows = [
        {
            'shapeID': ':book',
            'propertyID': 'dc:creator',
            'valueConstraint': '',
            'valueShape': ':author'
        }, {
            'shapeID': '',
            'propertyID': 'dc:type',
            'valueConstraint': 'so:Book',
            'valueShape': ''
        }, {
            'shapeID': ':author',
            'propertyID': 'foaf:name',
            'valueConstraint': '',
            'valueShape': ''
        }
    ]
    expected_shapes = [
        CSVShape(
            shapeID=':book',
            propertyID='dc:creator',
            valueConstraint='',
            valueShape=':author'
        ),
        CSVShape(
            shapeID='',
            propertyID='dc:type',
            valueConstraint='so:Book',
            valueShape=''
        ),
        CSVShape(
            shapeID=':author',
            propertyID='foaf:name',
            valueConstraint='',
            valueShape=''
        )
    ]
    assert _get_csvshapes(rows) == expected_shapes


#    csvrows_list = [
#        {
#            "shapeID": ":a",
#            "shapeLabel": "Book",
#            "shapeClosed": False,
#            "propertyID": "dct:creator",
#            "propertyLabel": "Creator",
#            "mandatory": True,
#            "repeatable": False,
#            "valueNodeType": "URI",
#            "valueDataType": "",
#            "valueConstraint": "",
#            "valueConstraintType": "",
#            "valueShape": ":b",
#            "note": "Typically the author.",
#        },
#        {
#            "shapeID": ":b",
#            "shapeLabel": "Person",
#            "shapeClosed": False,
#            "propertyID": "foaf:name",
#            "propertyLabel": "Name",
#            "mandatory": True,
#            "repeatable": False,
#            "valueNodeType": "String",
#            "valueDataType": "xsd:string",
#            "valueConstraint": "",
#            "valueConstraintType": "",
#            "valueShape": "",
#            "note": "",
#        },
#    ]
