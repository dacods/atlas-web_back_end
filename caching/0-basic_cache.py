#!/usr/bin/env python3
"""
A class that Inherits a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class that inherits the caching system
    """
    def put(self, key, item):
        """
        Assigns the item value for the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to the key
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
