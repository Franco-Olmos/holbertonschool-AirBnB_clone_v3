#!/usr/bin/python3
""" starts app """

from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

if __name__ == "__main__":
    h, p = '0.0.0.0', '5000'
    if getenv('HBNB_API_HOST'):
        h = getenv('HBNB_API_HOST')
    if getenv('HBNB_API_PORT'):
        p = getenv('HBNB_API_PORT')
    app.run(host=h, port=p, threaded=True)
