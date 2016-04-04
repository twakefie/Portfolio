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
import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class homeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write(template.render({'title': 'Home'}))

class aboutHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('templates/about.html')
		self.response.write(template.render({'title': 'About'}))

class resumeHandler(webapp2.RequestHandler):
	def get (self):
		template = JINJA_ENVIRONMENT.get_template('templates/resume.html')
		self.response.write(template.render({'title': 'Resume'}))

class projectHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('templates/projects.html')
		self.response.write(template.render({'title': 'Projects'}))

class photosHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('templates/photos.html')
		self.response.write(template.render({'title': 'Photos'}))

# class formHandler(webapp2.RequestHandler):
# 	def get(self):
# 		template = JINJA_ENVIRONMENT.get_template('templates/form.html')
# 		self.response.write(template.render({'title': 'Contact Form'}))



app = webapp2.WSGIApplication([
    ('/', homeHandler),
    ('/home.html', homeHandler),
    ('/about.html', aboutHandler),
    ('/resume.html', resumeHandler),
    ('/projects.html', projectHandler),
    ('/photos.html', photosHandler),
    
], debug=True)












