# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tiltCalculate(self, node):
        if not node: return 0
        return node.val + self.tiltCalculate(node.left) + self.tiltCalculate(node.right)

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        t_queue = []
        t_queue.append(root)
        b_tilt = 0
        while t_queue:
            t_node = t_queue.pop(0)
            b_tilt += abs(self.tiltCalculate(t_node.left) - self.tiltCalculate(t_node.right))
            if t_node.left: t_queue.append(t_node.left)
            if t_node.right: t_queue.append(t_node.right)
        return b_tilt