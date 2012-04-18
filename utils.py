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
        url = users.create_login_url(self.request.uri)
        anchor = 'Login'
        navbar[anchor] = url

    return navbar

def numericise(value):
    """
    >>> numericise("faa")
    'faa'
    >>> numericise("3")
    3
    >>> numericise("3.1")
    3.1
    >>> numericise("")
    0
    """

    try:
        value = int(value)
    except:
        try: 
            value = float(value)
        except:
            if value == "": 
                value = 0
    return value


if __name__ == '__main__':
    import doctest
    doctest.testmod()