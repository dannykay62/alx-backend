#!/usr/bin/python3
"""
    inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        use self.cache_data - dictionary from the parent class BaseCaching
        doesn't have limit
    """
    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
