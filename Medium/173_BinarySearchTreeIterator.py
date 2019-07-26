# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def stackGenerator(self, stack, node):
        if not node:
            return
        self.stackGenerator(stack, node.right)
        stack.append(node.val)
        self.stackGenerator(stack, node.left)

    def __init__(self, root):
        self.treeStack = []
        self.stackGenerator(self.treeStack, root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.treeStack.pop()

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return (self.treeStack != [])

t1, t2, t3, t4, t5 = TreeNode(7), TreeNode(3), TreeNode(15), TreeNode(9), TreeNode(20)
t1.left, t1.right = t2, t3
t3.left, t3.right = t4, t5
iterator = BSTIterator(t1)

