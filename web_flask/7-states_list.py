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


@app.route('/states_list', strict_slashes=False)
def all_states():
    """
        The rendered template with the 'states' variable passed as an argument.
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
