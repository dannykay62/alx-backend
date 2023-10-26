#!/usr/bin/python3
"""FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    - use self.cache_data - dictionary from the parent class BaseCaching
    - overload def __init__(self):
    """
    def __init__(self):
        super().__init__()
        self.data = {}
        self.next_in, self.next_out = 0, 0
    
    def _pop_element(self):
        """FIFO algorithm to remove element"""
        self.next_out += 1
        key = self.data[self.next_out]
        del self.data[self.next_out], self.cache_data[key]

    def _push_element(self, key, item):
        """FIFO algorithm to add element"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.next_out + 1]))
            self._pop_element()
        self.cache_data[key] = item
        self.next_in += 1
        self.data[self.next_in] = key

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push_element(key, item)

    def get(self, key):
        """return the value linked with the given key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
