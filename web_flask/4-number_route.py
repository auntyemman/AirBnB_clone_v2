#!/usr/bin/python3
""" A script that starts a Flask Web Application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a Message when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_variable(text):
    """Prints C followed by some variables"""
    new_text = text.replace('_', ' ')
    return 'C ' + new_text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """ Prints a Message when /python is called """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_variable(n):
    """Prints an integer number when /number is called"""
    return "{} is a number".format(n)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
