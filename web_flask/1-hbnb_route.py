#!/usr/bin/python3
"""
file: 1-hbnb_route.py
desc: This module runs a simple flask app.
Date Created: Nov 11, 2022
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB! from the root path"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB' from the /hbnb path"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
