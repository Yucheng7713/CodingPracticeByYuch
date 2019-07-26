# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue_iterative(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        r = root.val
        while root:
            if abs(root.val - target) < abs(r - target):
                r = root.val
            root = root.left if root.val > target else root.right
        return r

    def closestValue_recursive(self, root, target):
        r = root.val
        child = root.left if r > target else root.right
        if not child: return r
        cr = self.closestValue_iterative(child, target)
        return r if abs(r - target) < abs(cr - target) else cr

