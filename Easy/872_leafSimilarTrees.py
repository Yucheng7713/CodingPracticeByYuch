# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSequence(self, node, leafs):
        if not node:
            return
        elif not node.left and not node.right:
            leafs.append(node.val)
        self.leafSequence(node.left, leafs)
        self.leafSequence(node.right, leafs)
        return leafs

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leafSequence(root1, []) == self.leafSequence(root2, [])