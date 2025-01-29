#!/usr/bin/env python3
"""
Authentication
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a generated salt.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
