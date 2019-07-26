# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        t_queue, res = [root], []
        while t_queue:
            k = len(t_queue)
            res.append(t_queue[-1].val)
            for i in range(k):
                t_node = t_queue.pop(0)
                if t_node.left: t_queue += [t_node.left]
                if t_node.right: t_queue += [t_node.right]
        return res