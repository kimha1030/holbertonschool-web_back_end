#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def message() -> str:
    """ Method message """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ Method message """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Method login """
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        response_session = jsonify({"email": email, "message": "logged in"})
        response_session.set_cookie("session_id", session_id)
        return response_session


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Method that finds the user with session_id, if it exists,
        destroy the session and redirect to get (/). Otherwise,
        the response is 403 HTTP status """
    session_id = request.cookies.get("session_id")
    user_found = AUTH.get_user_from_session_id(session_id)
    if user_found:
        AUTH.destroy_session(user_found.id)
        red_to_get = "/"
        return redirect(red_to_get)
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ Method that finds the user with session_id, If the user exist,
        respond with a 200 HTTP status and JSON payload. Otherwise,
        the response is 403 HTTP status """
    session_id = request.cookies.get("session_id")
    user_found = AUTH.get_user_from_session_id(session_id)
    if user_found:
        return jsonify({"email": user_found.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ Method that search email field in form data. If email does not exist,
        the response is 403 HTTP status. Otherwise, generate a token and
        respond with a 200 HTTP status and JSON payload."""
    email = request.form.get("email")
    if email:
        new_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": new_token}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
