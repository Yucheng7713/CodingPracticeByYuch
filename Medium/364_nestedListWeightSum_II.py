# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
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

class Solution(object):
    def getDepth(self, nested_int, depth):
        if nested_int.isInteger():
            return depth
        d_depth = depth + 1
        for n_list in nested_int.getList():
            if not n_list.isInteger():
                d_depth = max(d_depth, self.getDepth(n_list, depth + 1))
        return d_depth

    def dfsSum(self, nested_int, depth):
        if nested_int.isInteger():
            return nested_int.getInteger() * depth
        d_sum = 0
        depth -= 1
        for n_list in nested_int.getList():
            if not n_list.isInteger():
                d_sum += self.dfsSum(n_list, depth)
            else:
                d_sum += n_list.getInteger() * depth
        return d_sum

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        d_depth = 1
        for n_list in nestedList:
            d_depth = max(d_depth, self.getDepth(n_list, 1))
        print(d_depth)
        result = 0
        for n_list in nestedList:
            result += self.dfsSum(n_list, d_depth)
        return result
