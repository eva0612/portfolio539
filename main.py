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
import jinja2
from google.appengine.ext.webapp import template
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        title = "Kehan Liao"
        css = "<link rel=\"stylesheet\" href=\"http://www.dowebok.com/demo/2014/77/css/jquery.fullPage.css\">"
        template_vars = {
            "title" : title,
            "name" : "HomeSlide",
            "css" : css
        }
        template = JINJA_ENVIRONMENT.get_template('HomeSlide.html')
        self.response.out.write(template.render(template_vars))


class ArtHandler(webapp2.RequestHandler):
    def get(self):
        title = "KL_Art"
        template_vars = {
          "title" : title,
          "name" : "Art"
        }
        template = JINJA_ENVIRONMENT.get_template('Art.html')
        self.response.out.write(template.render(template_vars))


class BioHandler(webapp2.RequestHandler):
    def get(self):
        title = "KL_Bio"
        template_vars = {
          "title" : title,
          "name" : "Biography"
        }
        template = JINJA_ENVIRONMENT.get_template('Biography.html')
        self.response.out.write(template.render(template_vars))


class ResumeHandler(webapp2.RequestHandler):
    def get(self):
        title = "KL_Resume"
        template_vars = {
          "title" : title,
          "name" : "Resume"
        }
        template = JINJA_ENVIRONMENT.get_template('Resume.html')
        self.response.out.write(template.render(template_vars))


class UXHandler(webapp2.RequestHandler):
    def get(self):
        title = "KL_UX"
        template_vars = {
          "title" : title,
          "name" : "UX"
        }
        template = JINJA_ENVIRONMENT.get_template('UX.html')
        self.response.out.write(template.render(template_vars))


class ErrorHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("<h1>Try a different URL;)</h1>")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Art', ArtHandler),
    ('/Biography', BioHandler),
    ('/Resume', ResumeHandler),
    ('/UX', UXHandler),
    ("/.*", ErrorHandler)

], debug=True)
