#!/usr/bin/env python3
"""Basic Flask app that use request.accept_languages"""
from flask import Flask, render_templates, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
"""Instantiate Babel object"""


class Config(object):
    """Configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" use the config class for the Flask app"""


@app.route('/')
def root():
    """home of the Flask app"""
    return render_templates("2-index.html")


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
