#!/usr/bin/env python3
"""
Task 4. Force locale with URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel
import os


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Babel configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("4-app.Config")


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome_msg():
    """ Method welcome_msg """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """ Method get_locale """
    session_language = request.args.get("locale")
    lang = app.config.get("LANGUAGES")
    if session_language in lang:
        return session_language
    else:
        return request.accept_languages.best_match(lang)


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
