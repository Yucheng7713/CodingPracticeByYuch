try:
    from DataStructure.LinkedList import LinkedList
except ImportError:
    print("Module not found")

class HashLinkedList(LinkedList):

    def containKey(self, key):
        temp = self.head
        while temp:
            if temp.val[0] == key:
                return True
            temp = temp.next
        return False

    def getValue(self, key):
        temp = self.head
        while temp:
            if temp.val[0] == key:
                return temp.val[1]
            temp = temp.next
        return None

    def setKeyValuePair(self, key, value):
        temp = self.head
        while temp:
            if temp.val[0] == key:
                temp.val = key, value
                break
            temp = temp.next

    def deleteKeyValuePair(self, key):
        temp = self.head
        delete_index = 0
        while temp:
            if temp.val[0] == key:
                break
            temp = temp.next
            delete_index += 1
        self.deleteAtIndex(delete_index)

class HashMap:
    # Components :
    # Nested array or array with linked lists - data structure used to store the data
    # Hash function (hash code) - function to convert key into array index
    # Collision handling - There are 2 ways :
        # 1 - Linear probing : if a hashed slot is occupied, move on to the next until reaching an empty slot.
        # 2 - Use a nested list for storage, keys with same hashing value get stored to the same array.
    # Hashing   O(1)
    # Put       O(1) amortized
    # Get       O(1) amortized
    # Contain   O(1) amortized
    # Delete    O(1) amortized

    def __init__(self, size):
        self.size = size
        self.hash_list = [HashLinkedList() for _ in range(size)]

    # For hash code we generate it by summing ASCII values of each character of the key
    def hashing(self, key):
        # return hash code as an integer
        return sum(ord(c) for c in key) % self.size

    def contain(self, key):
        # return Boolean
        hash_code = self.hashing(key)
        hash_list = self.hash_list[hash_code]
        return hash_list.containKey(key)

    def get(self, key):
        # return Object
        hash_code = self.hashing(key)
        return self.hash_list[hash_code].getValue(key)

    def put(self, key, value):
        hash_code = self.hashing(key)
        hash_list = self.hash_list[hash_code]
        if hash_list.containKey(key):
            hash_list.setKeyValuePair(key, value)
        else:
            hash_list.addAtTail((key, value))

    def delete(self, key):
        hash_code = self.hashing(key)
        hash_list = self.hash_list[hash_code]
        hash_list.deleteKeyValuePair(key)

if (__name__ == '__main__'):
    my_hash_table = HashMap(10)
    my_hash_table.put("Steven", 24)
    my_hash_table.put("nteveS", "Wonderful")
    my_hash_table.put("nvtSee", "1000")
    my_hash_table.put("CS", 100)
    my_hash_table.put("Great", "Hello World!!!")
    print(my_hash_table.get("Steven"))
    print(my_hash_table.get("nteveS"))
    print(my_hash_table.get("nvtSee"))
    my_hash_table.delete("nteveS")
    print(my_hash_table.get("nteveS"))
    print(my_hash_table.get("nvtSee"))
    print(my_hash_table.get("Steven"))
