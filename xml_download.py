from flask import send_file, Response, render_template, make_response
from flask_restful import Resource

class Download(Resource):
    def get(self):
      template = render_template('phonebook.xml')
      response = make_response(template)
      response.headers['Content-Type'] = 'application/xml'
      return response