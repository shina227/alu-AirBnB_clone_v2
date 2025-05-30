#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")  # Fetch fresh data
    return render_template("9-states.html", states=states)  # Pass as 'states'


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    states = storage.all("State")  # Fetch fresh data
    state = None
    for s in states.values():
        if s.id == id:
            state = s
            break  # Found the state, no need to keep looping
    return render_template("9-states.html", state=state)  # Pass as 'state'


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
