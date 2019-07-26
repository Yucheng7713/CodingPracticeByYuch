# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive way -> but the time complexity is high
class Solution_I(object):
    def traverseBST(self, n, lower, upper):
        if not n:
            return True
        return n.val > lower and n.val < upper and self.traverseBST(n.left, lower, n.val) and self.traverseBST(n.right, n.val, upper)

    def isValidBST(self, root):
        return self.traverseBST(root, float('-inf'), float('inf'))