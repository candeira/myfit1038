import cgi
import datetime
import urllib
import webapp2
import jinja2
import os

from google.appengine.ext import db
from google.appengine.api import users

import gspread

import private
from thespreadsheet import get_organised_data
from utils import logged_in, navbar

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Greeting(db.Model):
  """Models an individual Guestbook entry with an author, content, and date."""
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)


def guestbook_key(guestbook_name=None):
  """Constructs a datastore key for a Guestbook entity with guestbook_name."""
  return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')


class MainPage(webapp2.RequestHandler):
  def get(self):
    guestbook_name=self.request.get('guestbook_name')
    greetings_query = Greeting.all().ancestor(guestbook_key(guestbook_name)).order('-date')
    greetings = greetings_query.fetch(10)
    
    # this too should be an utility function
    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'
      
    template_values = {
      'greetings': greetings,
      'url': url,
      'url_linktext': url_linktext,
    }
    
    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))


class Guestbook(webapp2.RequestHandler):
  def post(self):
    # We set the same parent key on the 'Greeting' to ensure each greeting is in
    # the same entity group. Queries across the single entity group will be
    # consistent. However, the write rate to a single entity group should
    # be limited to ~1/second.
    guestbook_name = self.request.get('guestbook_name')
    greeting = Greeting(parent=guestbook_key(guestbook_name))

    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/?' + urllib.urlencode({'guestbook_name': guestbook_name}))


class Admin(webapp2.RequestHandler):
  """Where we check how everyone is doing.
  For now we replicate the spreadsheet view.
  Eventually we will have a panel kind of thing.
  """
  @logged_in(admin_only=True)
  def get(self):
    
    students = get_organised_data(private.spreadsheet)
    
    columns = ["ID", "Last Name", "First Name",	"Project Group", "UT1", "UT2", 
               "UT3", "Tute 3",	"Tute 4",	"Tute 6", "Tute 8", "Tute 9", 
               "Proposal",	"Recover",	"Presentation",	"Report",	"Final"]
    
    navbar_links = navbar(self)
    
    template_values = {"students": students.values(), "columns": columns,
                       "navbar_links": navbar_links}
      
    template = jinja_environment.get_template('admin.html')
    self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/admin', Admin),
                               ('/sign', Guestbook)],
                              debug=True)
