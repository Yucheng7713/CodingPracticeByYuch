class HashMap:
    # Components :
    # Array or Nested array - data structure used to store the data
    # Hash function - function to convert key into array index
    # Collision handling - There are 2 ways :
        # 1 - Linear probing : if a hashed slot is occupied, move on to the next until reaching an empty slot.
        # 2 - Use a nested list for storage, keys with same hashing value get stored to the same array.
    # Insert (Put)
    # Search (Get)
    # Delete

    STORAGE_SIZE = 100

    def __init__(self):
        self.hash_list = [[] for _ in range(self.STORAGE_SIZE)]

    def hashing(self, key):
        return sum([ord(c) for c in key]) % self.STORAGE_SIZE

    def get(self, key):
        h_key = self.hashing(key)
        bucket = self.hash_list[h_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                return v
        return None

    def put(self, key, item):
        h_key = self.hashing(key)
        key_exist = False
        bucket = self.hash_list[h_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                key_exist = True
                bucket[i] = (key, item)
                break
        if not key_exist:
            bucket.append((key, item))

    def delete(self, key):
        h_key = self.hashing(key)
        key_exist = False
        bucket = self.hash_list[h_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                key_exist = True
                del bucket[i]
                print("Deleted Key {}!".format(key))
                break
        if not key_exist:
            print("Key {} not found".format(key))


    def contain(self, key):
        if self.hash_list[self.hashing(key)]:
            return True
        return False

my_hash_table = HashMap()
my_hash_table.put("Steven", 24)
my_hash_table.put("CS", 100)
my_hash_table.put("Great", "Hello World!!!")
print(my_hash_table.get("Great"))
