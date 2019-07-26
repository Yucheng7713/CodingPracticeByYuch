class MyStack(object):
    def __init__(self):
        self.q_stack = []
        self.q_top = -1

    def push(self, x):
        # Push to back
        self.q_stack.append(x)
        self.q_top = x

    def pop(self):
        if self.q_stack == []:
            self.q_top = -1
            return self.q_top

        q_length = len(self.q_stack)
        for i in range(q_length):
            # Pop from the front
            c = self.q_stack.pop(0)
            if i < q_length - 1:
                self.q_stack.append(c)
                self.q_top = c
        return c

    def top(self):
        return self.q_top

    def empty(self):
        if self.q_stack == []:
            return True
        return False

stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())