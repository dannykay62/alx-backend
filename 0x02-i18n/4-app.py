#!/usr/bin/env python3
""" implement a way to force a particular locale by
    passing the locale=fr parameter to your app URLs
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)
"""instantiating the object of the babel"""


class Config(object):
    """Configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.configfrom_object(Config)
"""Use the Config class to config the Flask app"""


@app.route('/')
def root():
    """Flask app"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """Determine the best language match with our supported languages"""
    localLang = request.args.get('locale')
    supportLang = app.config['LANGUAGES']
    if localLang in supportLang:
        return localLang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    

if __name__ == "__main":
    app.run()
