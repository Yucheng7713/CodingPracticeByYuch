# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Use a previous pointer to track the head of flatten tree ( linked list )
    def __init__(self):
        self.prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.flatten(root.right)
        self.flatten(root.left)
        # Inorder to flatten the tree, we need to :
        # 1. Assign flatten tree to the right child of a node
        # 2. the left child of the node has to be set to None
        # Recursively do the above 2 steps.
        root.right = self.prev
        root.left = None
        self.prev = root