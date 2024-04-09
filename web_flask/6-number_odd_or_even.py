#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def text(text):
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text):
    text = text.replace('_', ' ')
    return "Python {}".format(text)

@app.route('/number/<n>', strict_slashes=False)
def numbers(n):
    if n.isdigit():
        return '{} is a number'.format(n)

@app.route('/number_template/<n>', strict_slashes=False)
def temp(n):
    if n.isdigit():
        return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def even_odd(n):
    if n.isdigit():
        if int(n) % 2 == 0:
            EvenOdd = "even"
        else:
            EvenOdd = "odd"
        return render_template('6-number_odd_or_even.html', n=n, EvenOdd=EvenOdd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)