# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allZeros(self, node):
        if not node: return True
        elif node.val == 1: return False
        return self.allZeros(node.left) and self.allZeros(node.right)
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or self.allZeros(root): return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root