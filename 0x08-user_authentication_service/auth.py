#!/usr/bin/env python3
"""
Auth
"""
import bcrypt


def _hash_password(password: str) -> str:
    """ Method that return a hashed password """
    salt = bcrypt.gensalt()
    p = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(p, salt)
    return hashedPassword
