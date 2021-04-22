#!/usr/bin/env python3
"""
Task 1. Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel
import os


app = Flask(__name__)
babel = Babel(app)


class Config():
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("1-app.Config")


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome_msg():
    """ Method welcome_msg """
    return render_template("0-index.html")


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
