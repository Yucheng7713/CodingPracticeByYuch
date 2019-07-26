class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.min_candidates = []
        self.min_element = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.min_stack.append(x)
        if self.min_element == None:
            self.min_element = x
        else:
            if self.min_element >= x:
                self.min_candidates.append(self.min_element)
                self.min_element = x

    def pop(self):
        """
        :rtype: void
        """
        if len(self.min_stack) > 0:
            if self.min_stack[-1] == self.min_element:
                if len(self.min_candidates) > 0:
                    self.min_element = self.min_candidates.pop()
                else:
                    self.min_element = None
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_element


#Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
param_4 = obj.getMin()
obj.pop()
param_4 = obj.getMin()

print(param_4)