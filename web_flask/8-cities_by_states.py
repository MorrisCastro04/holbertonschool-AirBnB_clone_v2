#!/usr/bin/python3
"""starts flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_states():
    """
    Renders a template that displays a list of cities grouped by states.
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_request
def teardown(self):
    """
    This function is a teardown function that is executed after each request.
    It closes the storage connection.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
