#!/usr/bin/env python3
"""
Auth
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar


def _hash_password(password: str) -> str:
    """ Method that return a hashed password """
    salt = bcrypt.gensalt()
    p = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(p, salt)
    return hashedPassword


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
