#!/usr/bin/env python3
"""
LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and implements LIFO caching
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.last = None

    def put(self, key, item):
        """
        Add item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last]
            print(f'DISCARD: {self.last}')

        self.last = key

    def get(self, key):
        """
        Return value linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
