# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_Diameter = 0
        def maxDepth(node):
            if not node: return 0
            left_max, right_max = maxDepth(node.left), maxDepth(node.right)
            self.max_Diameter = max(self.max_Diameter, left_max + right_max)
            return max(left_max, right_max) + 1
        maxDepth(root)
        return self.max_Diameter