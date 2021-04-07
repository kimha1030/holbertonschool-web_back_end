#!/usr/bin/env python3
""" Module of Session auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /api/v1/auth_session/login
    Return:
      - Dictionary of the user
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        user = User.search({'email': email})
        if not user:
            return jsonify({"error": "no user found for this email"}), 404
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    for u in user:
        if not u.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user[0].id)
    session_name = os.getenv('SESSION_NAME')
    res = jsonify(user[0].to_json())
    res.set_cookie(session_name, session_id)
    return res
