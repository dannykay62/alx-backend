#!/usr/bin/python3
"""LRUCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        use self.cache_data - dictionary from the parent class BaseCaching
        -  overload def __init__(self)
    """
    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """ LRU algorithm to handle elements"""
        self.next[head], self.prev[tail] = tail, head

    def remove_element(self, key):
        """LRU algorithm to remove an elment"""
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def add_element(self, key, item):
        """LRU algorithm to add an element"""
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)
        if len(self.cache_data) > BaseCaching:
            print("DISCARD: {}".format(self.next[self.head]))
            self.remove_element(self.next[self.head])

    def put_element(self, key, item):
        """Add element to the dictionary"""
        if key and item:
            if key in self.cache_data:
                self.remove_element(key)
            self.add_element(key, item)

    def get(self, key):
        """return the value linked to the key provided"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self.remove_element(key)
            self.add_element(key, value)
            return value
