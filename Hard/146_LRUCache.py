from collections import OrderedDict

# Design 1 - Inherit Python default OrderedDict
# The fresh used key will be maintained at the end
class LRUCache_I(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self: return -1
        # Refresh the called key
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            # Refresh the called key
            self.move_to_end(key)
        self[key] = value
        # If the capacity exceed -> remove the least used one
        if len(self) > self.capacity:
            self.popitem(last=False)

# Design 2 - Hash Map (Dict) + Linked List
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    # Doubled linked list operations
    # Add node to linked list
    def addNode(self, node):
        t = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        t.next = node
        node.prev = t
    # Remove node from linked list
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    # Move the given node to the end of the linked list
    def move_to_end(self, node):
        self.removeNode(node)
        self.addNode(node)

    # Remove the first node from the linked list
    def removeHead(self):
        removed_node = self.head.next
        self.removeNode(removed_node)
        return removed_node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head, self.tail = ListNode(0, 0), ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.move_to_end(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # Add new element to both dict and linked list
        if key not in self.cache:
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self.addNode(new_node)
        # The key's already existed, update the value, refresh the freshness
        else:
            self.cache[key].val = value
            self.move_to_end(self.cache[key])
        # After inserting new element, if the capacity exceeds,
        # Remove the least used node
        if len(self.cache) > self.capacity:
            r_node = self.removeHead()
            del self.cache[r_node.key]




            # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)