#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Inherits from BaseCaching and implements MRU caching
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            MRU_key = self.order.pop()
            del self.cache_data[MRU_key]
            print(f'DISCARD: {MRU_key}')

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Return value linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
