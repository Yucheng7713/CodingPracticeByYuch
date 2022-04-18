class ListStack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, item):
        self.stack.append(item)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        popped_item = self.stack.pop()
        self.length -= 1
        return popped_item

    def isEmpty(self):
        return self.length == 0