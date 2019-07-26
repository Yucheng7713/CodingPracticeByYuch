# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:

    def d_sum(self, nestedList, depth):
        w_sum = 0
        for i in nestedList:
            if i.getInteger():
                w_sum += i.getInteger() * depth
            else:
                w_sum += self.d_sum(i.getList(), depth + 1)
        return w_sum

    def depthSum(self, nestedList):
        return self.d_sum(nestedList, 1)

    def depthSum_II(self, nestedList):
        d_stack, d_sum = [], 0
        if nestedList == []:
            return d_sum
        for lst in nestedList:
            d_stack.append((lst, 1))
        while d_stack:
            d_element, depth = d_stack.pop()
            if d_element.isInteger():
                d_sum += d_element.getInteger() * depth
            else:
                for lst in d_element.getList():
                    d_stack.append((lst, depth + 1))
        return d_sum

    # Clever way to implement
    def depthSum_III(self, nestedList):
        res, depth = 0, 1
        while nestedList:
            res += sum([i.getInteger() for i in nestedList if i.isInteger()]) * depth
            nestedList = sum([l.getList() for l in nestedList if not l.isInteger()], [])
            depth += 1
        return res

# my_array = [[1, 2], [3, [4, 5]]]
# print(sum([i for i in my_array], []))

