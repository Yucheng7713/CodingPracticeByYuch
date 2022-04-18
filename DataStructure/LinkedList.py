# Definition of Linked list node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Get the element at index i
    def get(self, i):
        # If the given index is not available
        if i < 0 or i >= self.length:
            return None
        count, temp = i, self.head
        # Traverse the list from start searching for element i
        while count > 0:
            temp = temp.next
            count -= 1
        return temp.val

    # Append a new element at the start of the list
    def addAtHead(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        # If there is only one element in the list -> assign head and tail pointing to
        # the same element
        if not self.tail:
            self.tail = self.head
        self.length += 1

    # Append a new element at the end of the list
    def addAtTail(self, val):
        new_tail = Node(val)
        if self.tail:
            self.tail.next = new_tail
        self.tail = new_tail
        # If there is only one element in the list -> assign head and tail pointing to
        # the same element
        if not self.head:
            self.head = self.tail
        self.length += 1

    # Insert a new element before index i
    def addAtIndex(self, i, val):
        # Same as appending at the head
        if i == 0:
            self.addAtHead(val)
        # Same as appending at the tail
        elif i == self.length:
            self.addAtTail(val)
        # Only insert when i is available ( 0 < i < self.length )
        elif i > 0 and i < self.length:
            # Find the inserted position
            count, temp = i - 1, self.head
            while count > 0:
                temp = temp.next
                count -= 1
            # Insert the new element
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    # Delete the ith element from the list
    def deleteAtIndex(self, i):
        # Only delete when i is legit
        if i >= 0 or i < self.length:
            # Simply change the head index
            if i == 0:
                self.head = self.head.next
            else:
                # Find the deleted position.
                # For deleting ith position
                # We will change the next of (i - 1) pointing to its next.next
                # To pass through ith element
                count, temp = i - 1, self.head
                while count > 0:
                    temp = temp.next
                    count -= 1
                temp.next = temp.next.next
                # If the deleted element is actually the tail
                # then we need to update the current tail.
                if i == self.length - 1:
                    self.tail = temp
            self.length -= 1