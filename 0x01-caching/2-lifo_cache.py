#!/usr/bin/python3
"""LIFOCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ use self.cache_data - dictionary from the parent class BaseCaching
        overload def __init__(self):
    """
    def __init__(self):
        super().__init__()
        self.last_key = ''

    def put_element(self, key, item):
        """LIFO algorithm to add element to the dictionary"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """return the value linked to the key supplied"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
