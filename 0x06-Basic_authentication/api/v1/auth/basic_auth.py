#!/usr/bin/env python3
"""
basic_auth.py
"""
from api.v1.auth.auth import Auth
import base64
import typing
from models.user import User


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Method decode base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            dev = base64.b64decode(base64_authorization_header).decode("utf-8")
            return dev
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Method extract user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        list_data = decoded_base64_authorization_header.split(':')
        return (list_data[0], list_data[1])

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> typing.TypeVar('User'):
        """Method user object from credentials"""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            search_user = User.search({"email": user_email})
        except Exception:
            return None
        for user in search_user:
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None

    def current_user(self, request=None) -> typing.TypeVar('User'):
        """Method current user"""
        head_auth = self.authorization_header(request)
        if head_auth is None:
            return None
        ext_base64 = self.extract_base64_authorization_header(head_auth)
        if ext_base64 is None:
            return None
        dec_base64 = self.decode_base64_authorization_header(ext_base64)
        if dec_base64 is None:
            return None
        email, password = self.extract_user_credentials(dec_base64)
        if email is None or password is None:
            return None
        user_credentials = self.user_object_from_credentials(email, password)
        if user_credentials is None:
            return None
        else:
            return user_credentials
