
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

# List implementation ( inappropriate due to dequeue operation )
class ListQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * self.capacity

    # Enqueue takes constant time for appending.
    # Time complexity : O(1)
    def enqueue(self, item):
        if len(self.queue) == self.capacity:
            raise Exception("Queue capacity is full.")
        self.queue.append(item)

    # Inserting or deleting an element at the beginning requires shifting all of the other elements by one,
    # requiring time.
    # Time complexity : O(n) ---> X
    def dequeue(self):
        if not self.queue:
            raise Exception("Queue capacity is empty.")
        return self.queue.pop(0)

    # Return the front element in the queue.
    # Time complexity : O(1)
    def front(self):
        return self.queue[0]

    # Return the rear element in the queue.
    # Time complexity : O(1)
    def rear(self):
        return self.queue[-1]

# Deque implementation
class DequeQueue:

    def __init__(self, capacity):
        self.q = collections.deque(maxlen=capacity)

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
