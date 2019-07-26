# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        reverse = False
        t_queue, res = [root], []
        while t_queue:
            temp = []
            k = len(t_queue)
            for i in range(k):
                t_node = t_queue.pop(0)
                temp += [t_node.val]
                if t_node.left: t_queue += [t_node.left]
                if t_node.right: t_queue += [t_node.right]
            if reverse: res.append(temp[::-1])
            else: res.append(temp)
            reverse = not reverse
        return res