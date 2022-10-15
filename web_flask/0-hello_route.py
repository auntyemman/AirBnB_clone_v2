#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    retuen "Hello HBNB!”

if __main__ == "__name__":
    """IP and port app will run on"""
    app.run(host='0.0.0.0', port=5000)
