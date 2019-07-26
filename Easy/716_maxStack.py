from heapq import *

class MaxStack:
    def __init__(self):
        self.max_stack = []
        self.max_list = []

    def push(self, x):
        self.max_stack.append(x)
        if x not in self.max_list:
            self.max_list.append(x)
            self.max_list.sort()
        print("Max Stack : " + str(self.max_stack))
        # print("Max List : " + str(self.max_list))

    def pop(self):
        p = self.max_stack.pop()
        if p not in self.max_stack:
            p_index = self.max_list.index(p)
            self.max_list.remove(p)
        print("Max Stack : " + str(self.max_stack))
        # print("Max List : " + str(self.max_list))
        return p

    def top(self):
        print("Top > " + str(self.max_stack[-1]))
        return self.max_stack[-1]

    def peekMax(self):
        print("Max > " + str(self.max_list[-1]))
        return self.max_list[-1]

    def popMax(self):
        p_max = self.max_list[-1]
        max_index = len(self.max_stack) - self.max_stack[::-1].index(p_max) - 1
        self.max_stack.pop(max_index)
        if p_max not in self.max_stack:
            self.max_list.pop()
        print("Max Stack : " + str(self.max_stack))
        # print("Max List : " + str(self.max_list))
        return p_max



# Your MaxStack object will be instantiated and called as such:

obj = MaxStack()
obj.push(74)
obj.popMax()
obj.push(89)
obj.push(67)
obj.popMax()
obj.pop()
obj.push(61)
obj.push(-77)
obj.peekMax()
obj.popMax()
obj.push(81)
obj.pop()
obj.push(-71)
obj.push(32)