class HashMap:
    # Components :
    # Array - data structure used to store the data
    # Hash function - function to convert key into array index
    # Collision handling -
    STORAGE_SIZE = 100

    def __init__(self):
        self.hash_list = [None] * STORAGE_SIZE

    def hashing(self, key):
        return sum([ord(c) for c in key]) % STORAGE_SIZE

    def get(self, key):
        return self.hash_list[self.hashing(key)]

    def put(self, key, item):
        # Need to handle hashing collision here
        h_key = self.hashing(key)
        self.hash_list[h_key] = item

    def contain(self, key):
        if self.hashing(key):
            return True
        return False