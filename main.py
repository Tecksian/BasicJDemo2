#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import ndb
import jinja2
import webapp2
import os
from AustinClasses import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class MainHandler(webapp2.RequestHandler):
    #create an instance of our ConceptsPage class
    concepts_page = ConceptPage.query().get() #leaving the arguments blank to return everything.
                                              #As there is only one page, not an issue. Not great
                                              #coding practice, but fast for now.

    #check and see if the get() satement returned anything -- if it didn't, create the seed data
    #and then re-query/get
    if not concepts_page:
        concepts_page = ConceptPage()
        concepts_page.create_seed_data()

    def get(self):

        template_values = {
            'concepts_page': self.concepts_page,
        }

        template = jinja_env.get_template('concepts_page.html')
        self.response.write(template.render(template_values))

    def post(self):
        new_comment= self.request.get('new_comment')
        self.concepts_page.add_comment(new_comment)
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
