# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.leftSum = 0

    def sumLeftLeaveNodes(self, node):
        if not node:
            return 0
        elif node.left:
            if not node.left.right and not node.left.left:
                self.leftSum += node.left.val
        self.sumLeftLeaveNodes(node.left)
        self.sumLeftLeaveNodes(node.right)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumLeftLeaveNodes(root)
        return self.leftSum
