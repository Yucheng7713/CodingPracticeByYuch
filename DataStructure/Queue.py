
# Queue in Python can be implemented in the following ways :
# - List
# - collections.deque
# - queue.Queue

# Common operations associated with queue
# enqueue() : Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
#             Time complexity : O(1)
# dequeue() : Removes an item from the queue. The items are popped in the same order in which they are pushed.
#             If the queue is empty, then it is said to be an Underflow condition
#             Time complexity : O(1)
# front() : Get the front item from queue
#           Time complexity : O(1)
# rear() : Get the rear item from queue
#          Time complexity : O(1)

from collections import deque


class ListQueue:
    # List implementation (inappropriate due to dequeue operation)
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    # Enqueue takes constant time for appending.
    # Time complexity : O(1)
    def enqueue(self, item):
        if len(self.queue) == self.capacity:
            raise Exception("[WARNING] : Queue capacity is full.")
        self.queue.append(item)
        return True

    # Inserting or deleting an element at the beginning requires shifting all of the other elements by one,
    # requiring time.
    # Time complexity : O(n) ---> X
    def dequeue(self):
        if not self.queue:
            raise Exception("[WARNING] : Queue capacity is empty.")
        return self.queue.pop(0)

    # Return the front element in the queue.
    # Time complexity : O(1)
    def front(self):
        return self.queue[0]

    # Return the rear element in the queue.
    # Time complexity : O(1)
    def rear(self):
        return self.queue[-1]

    # Return the queue in string format
    # Time complexity : O(n)
    def output(self):
        return "->".join(self.queue)


class ListNode:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt


class LinkedListQueue:

    queueType = "LinkedList"

    # Linked list implementation
    def __init__(self, k):
        self.head = None
        self.tail = None
        self.maxSize = k
        self.size = 0

    def enqueue(self, element):
        if self.isFull():
            return False
        if self.tail:
            self.tail.nxt = ListNode(element, None)
            self.tail = self.tail.nxt
        else:
            self.head = ListNode(element, None)
            self.tail = self.head
        self.size += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            return False
        self.head = self.head.nxt
        if not self.head:
            self.tail = None
        self.size -= 1
        return True

    def front(self):
        if not self.head:
            return -1
        return self.head.val

    def end(self):
        if not self.tail:
            return -1
        return self.tail.val

    def isEmpty(self):
        return not self.head and not self.tail

    def isFull(self):
        return self.size == self.maxSize

    def __str__(self):
        index = self.head
        output = ""
        while index:
            output += str(index.val)
            if index.nxt:
                output += "->"
            index = index.nxt
        return output


# Deque implementation
class DequeQueue:

    def __init__(self, capacity):
        self.q = deque(maxlen=capacity)

    # Enqueue takes constant time for appending.
    # Time complexity : O(1)
    def enqueue(self, item):
        self.q.append(item)

    # Inserting or deleting an element at the beginning requires shifting all of the other elements by one,
    # requiring time.
    # Time complexity : O(1)
    def dequeue(self):
        return self.q.popleft()

    # Return the front element in the queue.
    # Time complexity : O(1)
    def front(self):
        return self.q[0]

    # Return the rear element in the queue.
    # Time complexity : O(1)
    def rear(self):
        return self.q[-1]

    # Return the queue in string format
    # Time complexity : O(n)
    def __str__(self):
        return "->".join(self.q)


q = LinkedListQueue(5)
q.enqueue("a")
q.enqueue("x")
q.enqueue("c")
q.enqueue("b")
q.enqueue("v")
q.dequeue()
q.enqueue("f")
print(q)