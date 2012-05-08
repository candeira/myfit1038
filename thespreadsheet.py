from collections import OrderedDict

import gspread

import private
from utils import dictify


def get_organised_data(spreadsheet=private.spreadsheet):
    """
    Test spreadsheet publically available at foo maybe
    >>> gspread_test = 'gspread test'
    >>> data = get_organised_data(gspread_test)
    >>> testdata = {}
    >>> testdata = {'Blargh!': 6.6, 'Foo': 1, 'Bar': 5.6, 'Email': 'me@example.com'}
    >>> data["me@example.com"] == testdata
    True

    """
    try:
        from Fit1038_Marking_2012 import data
    except ImportError:
        gc = gspread.login(private.username, private.password)
        wks = gc.open(spreadsheet).sheet1
        data = wks.get_all_values()

    return dictify(data)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

