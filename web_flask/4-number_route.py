#!/usr/bin/python3
"""starts flask web aplication"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns the string 'HBNB' when the '/hbnb' route is accessed.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """
    Converts the given text parameter by replacing
    underscores with spaces and returns it with a prefix 'C'.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text):
    """
    This function handles the '/python' route and the '/python/<text>' route.
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def numbers(n):
    """
    This function checks if the provided value is a
    number and returns a message accordingly.
    """
    if n.isdigit():
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
