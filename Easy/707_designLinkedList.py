class Node:
    def __init__(self, v):
        self.val = v
        self.next = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        # If the given index is not available
        if index < 0 or index >= self.length: return -1
        count = index
        temp = self.head
        # Locate the indexed element from head
        while count > 0:
            temp = temp.next
            count -= 1
        return temp.val

    def addAtHead(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        if not self.tail: self.tail = self.head
        self.length += 1

    def addAtTail(self, val):
        new_tail = Node(val)
        if self.tail:
            self.tail.next = new_tail
        self.tail = new_tail
        if not self.head: self.head = self.tail
        self.length += 1

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index > 0 and index < self.length:
            temp = self.head
            count = index - 1
            while count > 0:
                temp = temp.next
                count -= 1
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def deleteAtIndex(self, index):
        if index >= 0 and index < self.length:
            if index == 0:
                self.head = self.head.next
            else:
                temp = self.head
                count = index - 1
                while count > 0:
                    temp = temp.next
                    count -= 1
                temp.next = temp.next.next
                if index == self.length - 1:
                    self.tail = temp
            self.length -= 1


myList = MyLinkedList()
myList.addAtHead(1)
myList.addAtTail(3)
myList.addAtIndex(1, 2)
print(myList.get(1))
myList.deleteAtIndex(1)
print(myList.get(1))
