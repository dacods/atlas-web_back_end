#!/usr/bin/env python3
"""
Authentication
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound





class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def hash_password(self, password: str) -> bytes:
        """
        Hashes a password using bcrypt with a generated salt.
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user with a hashed password.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self.hash_password(password)
            return self._db.add_user(email, hashed_password)
    