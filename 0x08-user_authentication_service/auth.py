#!/usr/bin/env python3
"""
Auth
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Method that return a hashed password """
    salt = bcrypt.gensalt()
    p = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(p, salt)
    return hashedPassword


def _generate_uuid() -> str:
    """ Method that returns a string representation of a new UUID """
    repr_uuid = str(uuid4())
    return repr_uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Constructor """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method that returns a User object """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            h_password = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=h_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ Find the user by email. If it exists, check the password and
            if it matches return True. Otherwise, return False """
        try:
            user = self._db.find_user_by(email=email)
            p = password.encode("utf-8")
            check_pwd = bcrypt.checkpw(p, user.hashed_password)
            return check_pwd
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """ Method that returns the session ID as a string """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        self._db.update_user(user.id, session_id=_generate_uuid())
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """ Method that takes a single session_id string argument
            and returns the corresponding User or None """
        if session_id is None:
            return None
        try:
            user_found = self._db.find_user_by(session_id=session_id)
            return user_found
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Method takes a single user_id integer
            argument and returns None """
        if user_id is None:
            return None
        else:
            self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Method that finds the user corresponding to the email.
            If the user does not exist, raise a ValueError exception.
            If it exists, generate a UUID and update the user’s
            reset_token database field. Return the token. """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        self._db.update_user(user.id, reset_token=_generate_uuid())
        return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ Method that takes reset_token string argument and a password
            string argument and returns None """
        try:
            usr = self._db.find_user_by(reset_token=reset_token)
            pwd = _hash_password(password)
            self._db.update_user(usr.id, hashed_password=pwd, reset_token=None)
            return None
        except Exception:
            raise ValueError
