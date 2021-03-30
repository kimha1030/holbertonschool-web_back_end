#!/usr/bin/env python3
"""
auth.py
"""

from flask import request
import typing


class Auth():
    """Class auth"""

    def require_auth(self, path: str,
                     excluded_paths: typing.List[str]) -> bool:
        """methos requuire auth"""
        if not path:
            return True
        if not excluded_paths or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path = path + "/"
        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """method authorized header"""
        return None

    def current_user(self, request=None) -> typing.TypeVar('User'):
        """method current user"""
        return None
