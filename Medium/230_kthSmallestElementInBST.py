# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, node):
        if not node: return []
        return self.inorderTraversal(node.left) + [node.val] + self.inorderTraversal(node.right)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        inorderList = self.inorderTraversal(root)
        return inorderList[k - 1]