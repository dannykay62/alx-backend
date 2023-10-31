#!/usr/bin/env python3
"""A basic flask app with simple Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
"""Then instantiate the Babel object and Store it in a module-level variable"""


class Config(object):
    """Config class for languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
"""use the config class for the Flask app"""


@app.route('/')
def root():
    """a basic flask app"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
