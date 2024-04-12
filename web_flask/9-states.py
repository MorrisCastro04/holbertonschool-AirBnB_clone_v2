#!/usr/bin/python3
"""start the flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def takedown(self):
    """
    It is used to close the database connection after each request.
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_city(id=None):
    states = storage.all(State).values()
    state_name = None
    for state in states:
        if state.id == id:
            state_name = state
    return render_template("9-states.html", states=states, id=id,
                           state_name=state_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
