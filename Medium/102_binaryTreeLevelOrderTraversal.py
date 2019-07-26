# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        t_queue, res = [], []
        t_queue.append(root)
        while t_queue:
            l_nodes, temp_queue = [], []
            for i in range(len(t_queue)):
                t_node = t_queue.pop(0)
                l_nodes.append(t_node.val)
                if t_node.left: temp_queue.append(t_node.left)
                if t_node.right: temp_queue.append(t_node.right)
            t_queue = temp_queue
            res.append(l_nodes)
        return res