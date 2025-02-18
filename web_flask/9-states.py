#!/usr/bin/python3
"""
file: 9-states.py
Desc: This python module executes simple flask application.
Date Created: Nov 13, 2022
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def list_states(id=None):
    """Renders an html page with some State data stored in db"""
    states = storage.all("State")
    if id is None:
        return render_template("9-states.html", state=states)
    else:
        for state in states.values():
            if state.id == id:
                return render_template("9-states.html", state=state)
        return render_template("9-states.html")


@app.teardown_appcontext
def tear_down_db(execute):
    """Removes the current SQLAlchemy session after each request
    is completed"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
