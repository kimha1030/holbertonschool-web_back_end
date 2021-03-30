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
        if path and excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """method authorized header"""
        return None

    def current_user(self, request=None) -> typing.TypeVar('User'):
        """method current user"""
        return None
