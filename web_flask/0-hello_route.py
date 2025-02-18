#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/airbnb-onepage/')
def airbnb_onepage():
    return index()

