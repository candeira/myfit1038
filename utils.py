from collections import OrderedDict

from google.appengine.api import users

import private

def logged_in(admin_only=False):
  def f(g):
    return g
  return f
  
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

def numericise(value):
  """
  >>> numericise("faa")
  'faa'
  >>> numericise("3")
  3
  >>> numericise("3.1")
  3.1
  """
  try:
    value = int(value)
  except:
    try: 
      value = float(value)
    except:
      pass
  return value
  
if __name__ == '__main__':
    import doctest
    doctest.testmod()

