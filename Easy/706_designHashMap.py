class MyHashMap(object):
    def __init__(self):
        self.hash = [-1] * 1000001

    def put(self, key, value):
        self.hash[key] = value

    def get(self, key):
        return self.hash[key]

    def remove(self, key):
        self.hash[key] = -1