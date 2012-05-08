from collections import OrderedDict

from google.appengine.api import users

import private

def logged_in(admin_only=False):
    def decorator(g):
        def decorated(self):
            user = users.get_current_user()
            if not user:
                return self.redirect(users.create_login_url(self.request.uri))
            elif admin_only:
                if user.nickname() not in private.admins:
                    return self.redirect('/')
            
            return g(self)
        return decorated
    return decorator
  
def navbar(handler):
    """Returns a dictionary of anchor:urls for the navbar"""
    navbar = OrderedDict()
    user = users.get_current_user()
    if user: 
        if user.nickname() in private.admins:
            anchor = "Admin"
            url = "/admin"
            navbar[anchor] = url
        url = users.create_logout_url(handler.request.uri)
        anchor = 'Logout'
        navbar[anchor] = url
    else:
        url = users.create_login_url(handler.request.uri)
        anchor = 'Login'
        navbar[anchor] = url

    return navbar

def numericise(value, blank2zero=True):
    """
    >>> numericise("faa")
    'faa'
    >>> numericise("3")
    3
    >>> numericise("3.1")
    3.1
    >>> numericise("")
    0
    >>> numericise("", blank2zero=False)
    ''
    """

    try:
        value = int(value)
    except:
        try: 
            value = float(value)
        except:
            if value == "" and blank2zero == True: 
                value = 0
    return value

def dictify(data, blanks2zeros=True):
    # we have a list of lists that looks like this:
    # [[ "Name"   , "email"              , "grade_foo"  ], < keys for dictionary
    #  [ "javier" , "candeira@gmail.com" , "10"         ], < start of values
    #  [ "Mary"   , "mary@monash.edu"    , "9"          ]]
    #
    # and we turn it into a dict of dicts that looks like this:
    # { "candeira@gmail.com": {"Name": "javier", "email": "candeira@gmail.com", etc... }
    #   "mary@monash.edu"   : {"Name": "Mary"  , "email": "mary@monash.edu", etc... } 
    #    etc... }
    
    wks_keys = data[0]
    dictified = OrderedDict()
    for row in data[1:]:
        # first, convert numericisable string values into numeric values
        row = [numericise(v, blanks2zeros) for v in row]
        student = dict(zip(wks_keys,row))
        dictified[student["Email"]] = student
    return dictified


if __name__ == '__main__':
    import doctest
    doctest.testmod()