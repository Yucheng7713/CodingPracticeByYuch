# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        return self.maxDepthExplore(root, 0)
    def maxDepthExplore(self, root, currentMax):
        if root == None:
            return currentMax
        currentMax += 1
        return max(self.maxDepthExplore(root.left, currentMax), self.maxDepthExplore(root.right, currentMax))