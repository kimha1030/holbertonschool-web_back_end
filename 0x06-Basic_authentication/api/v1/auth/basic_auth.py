#!/usr/bin/env python3
"""
basic_auth.py
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class BasicAuth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Method extract base 64 authorization"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.startswith("Basic "):
            sec_word = authorization_header.split(' ')[1]
            return sec_word
        else:
            return None
