class MyQueue(object):
    def __init__(self):
        self.s_queue = []
        self.front = -1

    def push(self, x):
        if self.s_queue == []:
            self.front = x
        self.s_queue.append(x)

    def pop(self):
        if self.s_queue == []:
            self.front = -1
            return self.front
        inverted_stack = []
        while self.s_queue != []:
            inverted_stack.append(self.s_queue.pop())
        k = inverted_stack.pop()
        if inverted_stack == []:
            self.front = -1
            self.s_queue = inverted_stack
        else:
            self.front = inverted_stack[-1]
            while inverted_stack != []:
                self.s_queue.append(inverted_stack.pop())
        return k

    def peek(self):
        return self.front

    def empty(self):
        if self.s_queue == []:
            return True
        return False


class MyQueue_II(object):
    def __init__(self):
        self.s_queue, self.i_queue = [], []

    def push(self, x):
        self.s_queue.append(x)

    def pop(self):
        if self.i_queue == []:
            while self.s_queue != []:
                self.i_queue.append(self.s_queue.pop())
        return self.i_queue.pop()

    def peek(self):
        if self.i_queue == []:
            while self.s_queue != []:
                self.i_queue.append(self.s_queue.pop())
        return self.i_queue[-1]

    def empty(self):
        return (self.s_queue == []) and (self.i_queue == [])