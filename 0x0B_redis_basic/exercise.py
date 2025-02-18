#!/usr/bin/env python3
"""

"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    
    """
    def __init__(self) -> None:
        """"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[bytes, str, int, float, None]:
        """
        
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        
        """
        return self.get(key, lambda v: v.decode('utf-8'))

    def get_int(self, key:str) -> Optional[int]:
        """
        
        """
        return self.get(key, lambda v: int(v))
