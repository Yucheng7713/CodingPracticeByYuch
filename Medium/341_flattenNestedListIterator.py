# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.n_stack = nestedList

    # For each next() call, we ensure that it will be integer.
    def next(self):
        """
        :rtype: int
        """
        return self.n_stack.pop(0).getInteger()

    # If there is next "integer" to get
    # If it is a nested list instead, parse it and appended by the rest array
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.n_stack:
            top = self.n_stack[0]
            if top.isInteger():
                return True
            # Flatten
            self.n_stack = top.getList() + self.n_stack[1:]
        return False

        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())