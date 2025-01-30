#!/usr/bin/env python3
"""
Authentication
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a generated salt.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def _generate_uuid() -> str:
    """
    Generates a new UUID and returns its string representation.
    """
    return str(uuid.uuid4())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user with a hashed password.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a user's login credentials.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False
