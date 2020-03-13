from flask import Flask
from flask_restful import Api
import xml_download
import os

app = Flask(__name__)
app.secret_key = "VERY-CONFIDENTAL"
api = Api(app)

api.add_resource(xml_download.Download, "/phonebook.xml")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)