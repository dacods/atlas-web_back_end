#!/usr/bin/env python3
"""
FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and implements FIFO caching
    """
    def __init__(self):
        """
        Initialize the class and create a structure to track the key order
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add item in cache using FIFO
        Delete the oldest item if cache exceeds MAX_ITEMS
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest = self.order.pop(0)
            del self.cache_data[oldest]
            print(f'DISCARD: {oldest}')

    def get(self, key):
        """
        Return value linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
