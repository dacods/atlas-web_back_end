#!/usr/bin/env python3
"""
LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits from BaseCaching and implements LIFO caching
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

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            LRU_key = self.order.pop(0)
            del self.cache_data[LRU_key]
            print(f'DISCARD: {LRU_key}')

    def get(self, key):
        """
        Return value linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
