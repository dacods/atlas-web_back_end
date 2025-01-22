#!/usr/bin/env python3
"""
A class that Inherits a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Returns the cache data
    """
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
