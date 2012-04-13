
import gspread

import private
from utils import numericise


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
    gc = gspread.login(private.username, private.password)
    wks = gc.open(spreadsheet).sheet1
    data = wks.get_all_values()

    # we have a list of lists that looks like this:
    # [[ "Name"   , "email"              , "grade_foo"  ], < keys for dictionary
    #  [ "javier" , "candeira@gmail.com" , "10"         ], < special values
    #  [ "Mary"   , "mary@monash.edu"    , "9"          ]]
    #
    # and we turn it into a dict of dicts that looks like this:
    # { "candeira@gmail.com": {"Name": "javier", "email": "candeira@gmail.com", etc... }
    #   "mary@monash.edu"   : {"Name": "Mary"  , "email": "mary@monash.edu", etc... } 
    #    etc... }
    
    wks_keys = data[0]
    del data[0]
    students = {}
    for row in data:
      # first, convert numericisable string values into numeric values
      row = [numericise(v) for v in row]
      student = dict(zip(wks_keys,row))
      students[student["Email"]] = student
      
    return students
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

