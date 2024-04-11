#!/usr/bin/python3
"""starts Flask web aplication"""
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
    This function is a route handler for the '/hbnb' endpoint.
    It returns the string 'HBNB' as the response.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text):
    """
    This function handles the '/python' route and any additional text provided.
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
