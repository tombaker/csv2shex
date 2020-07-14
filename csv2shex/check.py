"""Check CSV file structure for anomalies"""


from .mkstatements import csvreader, list_statements


def check(csvfile):
    """Check CSV file structure for anomalies"""
    for statement in list_statements(csvreader(csvfile)):
        statement._is_uristem_used_correctly()
