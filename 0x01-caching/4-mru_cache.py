#!/user/bin/python3
"""inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ use self.cache_data - dictionary from the parent class BaseCaching
        You can overload def __init__(self)
    """
    def __init__(self):
        super().__init__()
        self.head, self.tail = 'head', 'tail'
        self.next, self.prev = {}, {}
        self.do(self.head, self.tail)

    def do(self, head, tail):
        """MRU algorithm to handle the elements"""
        self.next[head], self.prev[tail] = tail, head

    def remove_element(self, key):
        """MRU allgorithm to remove elements"""
        self.do(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def add_element(self, key, item):
        """algorithm to add element to the cache"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.prev[self.tail]))
            self.remove_element(self.prev[self.tail])
        self.cache_data[key] = item
        self.do(self.prev[self.tail], key)
        self.do(key, self.tail)

    def put_element(self, key, item):
        """assign element to the dictionary"""
        if key and item:
            if key in self.cache_data:
                self.remove_element(key)
            self.add_element(key, item)

    def get(self, key):
        """return the value linked to the key supplied"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self.remove_element(key)
            self.add_element(key, value)
            return value
