class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isempty():
            return self.queue.pop(0)
        return None

    def isempty(self):
        return self.queue == []