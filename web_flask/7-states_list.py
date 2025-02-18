#!/usr/bin/python3
"""
file: 7-states_list.py
Desc: This python module executes simple flask application.
Date Created: Nov 12, 2022
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Renders an html page with some State data stored in db"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_down_db(execute):
    """Removes the current SQLAlchemy session after each request
    is completed"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
