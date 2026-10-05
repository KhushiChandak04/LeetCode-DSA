from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        #maximum size of cache
        self.capacity = capacity

        #stores key and value
        self.cache = OrderedDict()

    def get(self, key):
        #if key is not there
        if key not in self.cache:
            return -1

        #get the value
        value = self.cache[key]

        #delete key and add it again this makes it the most recently used
        del self.cache[key]
        self.cache[key] = value

        return value

    def put(self, key, value):
        #if key already exists, delete it
        if key in self.cache:
            del self.cache[key]

        #add key at the end
        self.cache[key] = value

        #if cache is too big
        if len(self.cache) > self.capacity:
            #remove first key = least recently used
            self.cache.popitem(last=False)