#!/usr/bin/env python3
"""
API authentication
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """
    Class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        """
        if path is None or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current authenticated user.
        """
        return None

    def session_cookie(self, request=None):
        """
        Retrieves the session cookie from the request.
        """
        if request is None:
            return None

        session_name = os.getenv("SESSION_NAME", "_my_session_id")
        return request.cookies.get(session_name)
