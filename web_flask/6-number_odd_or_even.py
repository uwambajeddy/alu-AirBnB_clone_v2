#!/usr/bin/python3
"""
file: 5-number_template.py
desc: This module runs a simple flask app.
Date Created: Nov 11, 2022
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB! from the root path"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB' from the /hbnb path"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """Displays C <text>, replaces any _ with space"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythontext(text="is cool"):
    """Displays 'Python <text>', replaces any _ with space"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """Displays '<n> is a number' only if n is number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_for_n(n):
    """Renders an html page if n is a number"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Renders an html page if n is a number, also it specifies
    wheather the number is odd or even"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
