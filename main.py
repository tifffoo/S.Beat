import webapp2
import jinja2
import os
import logging
import requests
import time

# import config

from google.appengine.api import users
from google.appengine.ext import ndb

class Person(ndb.Model):
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    history = ndb.StringProperty()

class Query(ndb.Model):
    search_term = ndb.StringProperty()
    source1 = ndb.StringProperty()
    source2 = ndb.StringProperty()
    source1_name = ndb.StringProperty()
    source2_name = ndb.StringProperty()
    personKey = ndb.KeyProperty()
    time_searched = ndb.DateTimeProperty(auto_now_add=True)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):

        # search_term = self.request.get("search_term")
        # source1 = self.request.get("source1")
        # source2 = self.request.get("source2")

        #login
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }

        template = env.get_template("templates/main.html")
        self.response.write(template.render(templateVars))
        # logging.info(response.json())

class ClickMe(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/division_1newnew.html")
        self.response.write(template.render(templateVars))

class Profile(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
            if not current_person:
                current_person = Person(email=current_email)
                current_person.put()
        else:
            self.redirect('/')
            current_person = None

        logout_url = users.create_logout_url('/')
        templateVars = {}

        try:
            # person variable
            query_query = Query.query()
            query_query = Query.query().filter(Query.personKey == current_person.key)
            query_query = query_query.order(-Query.time_searched)
            queries = query_query.fetch(limit=20) #######3

            templateVars = {
                'current_user': current_user,
                'logout_url': logout_url,
                'queries' : queries,

            }
        except AttributeError:
            self.redirect('/')

        template = env.get_template('templates/profile.html')
        self.response.write(template.render(templateVars))

class CreateAccount(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        current_user = users.get_current_user()
        email = current_user.email()
        person = Person(name=name, email=email)
        person.put()
        time.sleep(2) #to fix the delay refresh
        self.redirect('/')

# class ResultsPage(webapp2.RequestHandler):
#     def get(self):
#         current_user = users.get_current_user()
#         people = Person.query().fetch()
#
#         if current_user:
#             current_email = current_user.email()
#             current_person = Person.query().filter(Person.email == current_email).get()
#             if not current_person:
#                 current_person = Person(email=current_email)
#                 current_person.put()
#             source1_name = to_name(source1)
#             query = Query(search_term=search_term, source1=source1, source2=source2, source1_name=source1_name,
#                 source2_name=source2_name, personKey=current_person.key)
#             query.put()
#         else:
#             current_person = None
#
#         templateVars = {
#              "current_person" : current_person,
#              "current_user" : current_user,
#         }
#
#         template = env.get_template('templates/results.html')
#         self.response.write(template.render(templateVars))

class About(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()
        if current_user:
            current_email = current_user.email() #?
        else:
            current_person = None
        logout_url = users.create_logout_url('/')
        templateVars = {
            'current_user': current_user,
            'logout_url': logout_url,
        }
        template = env.get_template("templates/about.html")
        self.response.write(template.render(templateVars))

class SpecificLocal(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()

        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/Division_2.2.html")
        self.response.write(template.render(templateVars))

class Eyes(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/Division_3.1.html")
        self.response.write(template.render(templateVars))

class Stomach(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/Division_3.3.html")
        self.response.write(template.render(templateVars))

class Genital(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/division_3.4.html")
        self.response.write(template.render(templateVars))

class Knee(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/Division_3.5.html")
        self.response.write(template.render(templateVars))

class Foot(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/Division_3.2.html")
        self.response.write(template.render(templateVars))

class Throat(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/Division_3.6.html")
        self.response.write(template.render(templateVars))

class Eye1(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/pinkeye.html")
        self.response.write(template.render(templateVars))

# class LsSymptoms(webapp2.RequestHandler):
#     def get(self):
#         login_url = ''
#         logout_url = ''
#         current_user = users.get_current_user()
#         people = Person.query().fetch()
#         if current_user:
#             current_email = current_user.email() #?
#             current_person = Person.query().filter(Person.email == current_email).get()
#         else:
#             current_person = None
#
#         login_url = users.create_login_url('/profile')
#         logout_url = users.create_logout_url('/')
#         templateVars = {
#             # For the login
#             'people': people,
#             'current_user': current_user,
#             'login_url': login_url,
#             'logout_url': logout_url,
#             'current_person': current_person,
#         }
#         template = env.get_template("templates/Common_symptoms.html")
#         self.response.write(template.render(templateVars))

class SevereSymptoms(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("division_2comvsseve")
        self.response.write(template.render(templateVars))

class Common(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/Common_symptoms.html")
        self.response.write(template.render(templateVars))

class c_diag(webapp2.RequestHandler):
    def get(self):
        login_url = ''
        logout_url = ''
        current_user = users.get_current_user()
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email() #?
            current_person = Person.query().filter(Person.email == current_email).get()
        else:
            current_person = None

        login_url = users.create_login_url('/profile')
        logout_url = users.create_logout_url('/')
        templateVars = {
            # For the login
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'current_person': current_person,
        }
        template = env.get_template("templates/common_diagnosis.html")
        self.response.write(template.render(templateVars))
    # class Throat1(webapp2.RequestHandler):
    #     def get(self):
    #         login_url = ''
    #         logout_url = ''
    #         current_user = users.get_current_user()
    #         people = Person.query().fetch()
    #         if current_user:
    #             current_email = current_user.email() #?
    #             current_person = Person.query().filter(Person.email == current_email).get()
    #         else:
    #             current_person = None
    #
    #         login_url = users.create_login_url('/profile')
    #         logout_url = users.create_logout_url('/')
    #         templateVars = {
    #             # For the login
    #             'people': people,
    #             'current_user': current_user,
    #             'login_url': login_url,
    #             'logout_url': logout_url,
    #             'current_person': current_person,
    #         }
    #         template = env.get_template("templates/.html")
    #         self.response.write(template.render(templateVars))
    #
    #     class Foot1(webapp2.RequestHandler):
    #         def get(self):
    #             login_url = ''
    #             logout_url = ''
    #             current_user = users.get_current_user()
    #             people = Person.query().fetch()
    #             if current_user:
    #                 current_email = current_user.email() #?
    #                 current_person = Person.query().filter(Person.email == current_email).get()
    #             else:
    #                 current_person = None
    #
    #             login_url = users.create_login_url('/profile')
    #             logout_url = users.create_logout_url('/')
    #             templateVars = {
    #                 # For the login
    #                 'people': people,
    #                 'current_user': current_user,
    #                 'login_url': login_url,
    #                 'logout_url': logout_url,
    #                 'current_person': current_person,
    #             }
    #             template = env.get_template("templates/pinkeye.html")
    #             self.response.write(template.render(templateVars))
    #
    #         class Genetial1(webapp2.RequestHandler):
    #             def get(self):
    #                 login_url = ''
    #                 logout_url = ''
    #                 current_user = users.get_current_user()
    #                 people = Person.query().fetch()
    #                 if current_user:
    #                     current_email = current_user.email() #?
    #                     current_person = Person.query().filter(Person.email == current_email).get()
    #                 else:
    #                     current_person = None
    #
    #                 login_url = users.create_login_url('/profile')
    #                 logout_url = users.create_logout_url('/')
    #                 templateVars = {
    #                     # For the login
    #                     'people': people,
    #                     'current_user': current_user,
    #                     'login_url': login_url,
    #                     'logout_url': logout_url,
    #                     'current_person': current_person,
    #                 }
    #                 template = env.get_template("templates/pinkeye.html")
    #                 self.response.write(template.render(templateVars))
    #         class Knee1(webapp2.RequestHandler):
    #             def get(self):
    #                 login_url = ''
    #                 logout_url = ''
    #                 current_user = users.get_current_user()
    #                 people = Person.query().fetch()
    #                 if current_user:
    #                     current_email = current_user.email() #?
    #                     current_person = Person.query().filter(Person.email == current_email).get()
    #                 else:
    #                     current_person = None
    #
    #                 login_url = users.create_login_url('/profile')
    #                 logout_url = users.create_logout_url('/')
    #                 templateVars = {
    #                     # For the login
    #                     'people': people,
    #                     'current_user': current_user,
    #                     'login_url': login_url,
    #                     'logout_url': logout_url,
    #                     'current_person': current_person,
    #                 }
    #                 template = env.get_template("templates/pinkeye.html")
    #                 self.response.write(template.render(templateVars))
    #
    #             class Eye1(webapp2.RequestHandler):
    #                 def get(self):
    #                     login_url = ''
    #                     logout_url = ''
    #                     current_user = users.get_current_user()
    #                     people = Person.query().fetch()
    #                     if current_user:
    #                         current_email = current_user.email() #?
    #                         current_person = Person.query().filter(Person.email == current_email).get()
    #                     else:
    #                         current_person = None
    #
    #                     login_url = users.create_login_url('/profile')
    #                     logout_url = users.create_logout_url('/')
    #                     templateVars = {
    #                         # For the login
    #                         'people': people,
    #                         'current_user': current_user,
    #                         'login_url': login_url,
    #                         'logout_url': logout_url,
    #                         'current_person': current_person,
    #                     }
    #                     template = env.get_template("templates/pinkeye.html")
    #                     self.response.write(template.render(templateVars))
    #
    #                 class Somach1(webapp2.RequestHandler):
    #                     def get(self):
    #                         login_url = ''
    #                         logout_url = ''
    #                         current_user = users.get_current_user()
    #                         people = Person.query().fetch()
    #                         if current_user:
    #                             current_email = current_user.email() #?
    #                             current_person = Person.query().filter(Person.email == current_email).get()
    #                         else:
    #                             current_person = None
    #
    #                         login_url = users.create_login_url('/profile')
    #                         logout_url = users.create_logout_url('/')
    #                         templateVars = {
    #                             # For the login
    #                             'people': people,
    #                             'current_user': current_user,
    #                             'login_url': login_url,
    #                             'logout_url': logout_url,
    #                             'current_person': current_person,
    #                         }
    #                         template = env.get_template("templates/pinkeye.html")
    #                         self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ('/', HomePage), #this maps the root url to the MainPage Handler
    ('/about', About),
    ('/profile', Profile),
    ('/create', CreateAccount),
    ('/div1', ClickMe),
    ('/div2', SpecificLocal),
    ('/div3.1', Eyes),
    ('/stomach', Stomach),
    ('/genital', Genital),
    ('/knee', Knee),
    ('/foot', Foot),
    ('/throat', Throat),
    ('/pinkeye', Eye1),
    # ('/div2.2', LsSymptoms),
    ('/div2.2.1', SevereSymptoms),
    ('/commonsympt', Common),
    ('/commondiag', c_diag),
    # ('/results', ResultsPage),
    # # ('/question1', Body/Gen),
    # # ('/body', Body),
    # # ('/general', General),
], debug=True)
