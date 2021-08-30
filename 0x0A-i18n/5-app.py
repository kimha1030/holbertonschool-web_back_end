from typing import type_check_only


#!/usr/bin/env python3
"""
Task 5. Mock logging in
"""
from flask import Flask, render_template, request
from flask_babel import Babel
import os
import typing


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Babel configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("5-app.Config")


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome_msg():
    """ Method welcome_msg """
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """ Method get_locale """
    session_language = request.args.get("locale")
    lang = app.config.get("LANGUAGES")
    if session_language in lang:
        return session_language
    else:
        return request.accept_languages.best_match(lang)

def get_user() -> typing.Union[dict, None]:
    """ Method get_user """
    req_login = request.args.get('login_as')
    if req_login:
        usr = int(req_login)
        if usr in users:
            return users.get(usr)
    else:
        return None

@app.before_request
def before_request():
    """ Method before_request """
    g.user = get_user()


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
