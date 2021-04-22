#!/usr/bin/env python3
"""
Task 0. Basic Flask App
"""
from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome_msg():
    """ Method index"""
    return render_template("0-index.html")


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
