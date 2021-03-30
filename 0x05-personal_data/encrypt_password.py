#!/usr/bin/env python3
"""
encrypt_password.py
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Method that returns a salted, hashed
        password, which is a byte string. """
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd, salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Method that validates that the provided password
        matches the hashed password """
    pwd = password.encode('utf-8')
    if bcrypt.checkpw(pwd, hashed_password):
        return True
    else:
        return False
