#!/usr/bin/python3
"""start Flask web aplication"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function is a route handler for the root URL ("/").
    It returns the string 'Hello HBNB!' as the response.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function handles the '/hbnb' route and returns the string 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """
    Display 'C' followed by the value of the 'text' parameter.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
