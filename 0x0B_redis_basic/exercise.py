#!/usr/bin/env python3
"""

"""
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper

def replay(self, method: Callable) -> None:
    """
    
    """
    redis_instance = method.__self__._redis

    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = self._redis.lrange(input_key, 0, -1)
    outputs = self._redis.lrange(output_key, 0, -1)

    call_count = redis_instance.get(method.__qualname__).decode("utf-8")

    print(f"{method.__qualname__} was called {call_count} times:")
    for input_data, output_data in zip(inputs, outputs):
        printf(f"{method.__qualname__}(*{input_data.decode('utf-8')}) -> {output_data.decode('utf-8')}")

class Cache:
    """
    
    """
    def __init__(self) -> None:
        """"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
