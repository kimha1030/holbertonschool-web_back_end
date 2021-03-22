#!/usr/bin/python3
"""Class MRUCache"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Class MRUCache that inherits from BaseCaching
        and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.list_keys = []

    def put(self, key, item):
        """Method put"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.list_keys:
                self.list_keys.append(key)
            else:
                self.list_keys.remove(key)
                self.list_keys.append(key)
            if len(self.list_keys) > BaseCaching.MAX_ITEMS:
                recentKeyDel = self.list_keys.pop(-2)
                del self.cache_data[recentKeyDel]
                print("DISCARD: {}".format(recentKeyDel))

    def get(self, key):
        """Method get"""
        if key is not None and key in self.cache_data:
            self.list_keys.remove(key)
            self.list_keys.append(key)
            return self.cache_data[key]
        else:
            return None
