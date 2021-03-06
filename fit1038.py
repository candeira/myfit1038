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
from utils import logged_in, navbar, numericise

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
  """The student view of their grades"""

  @logged_in()
  def get(self):
    user = users.get_current_user()
    email = user.nickname()
    
    students = get_organised_data(private.spreadsheet)
    
    if email not in students.keys():
      return self.redirect(users.create_logout_url(self.request.uri))
    
    student = students[email]
    # fake student candeira holds the max grades for the whole unit
    # fake student campbell holds the max grades for assessments up to the current date
    max_grade = students['candeira']
    max_so_far = students['campbell.wilson@monash.edu']

    def consolidate(student):
        """Commodity function just for the side effects"""
        student['Tutorials'] = sum(student[tute] for tute in ["Tute 3", "Tute 4", "Tute 6", "Tute 8", "Tute 9"])
        return

    consolidate(student)
    consolidate(max_grade)
    consolidate(max_so_far)  

    available = max_grade['Final'] - max_so_far['Final']
    
    columns = ["UT1", "UT2", "UT3", "Tutorials", "Proposal", "Presentation",	"Report",	"Final"]  
    
    navbar_links = navbar(self)
      
    template_values = {
      'columns': columns,
      'student': student,
      'max_grade': max_grade,
      'navbar_links': navbar_links,
      'available' : available,
    }
    
    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))



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
               "Proposal",	"Presentation",	"Report",	"Final"]
    
    navbar_links = navbar(self)

    template_values = {"students": students.values(), 
                       "columns": columns,
                       "navbar_links": navbar_links}
      
    template = jinja_environment.get_template('admin.html')
    self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/admin', Admin)],
                               debug=True)
