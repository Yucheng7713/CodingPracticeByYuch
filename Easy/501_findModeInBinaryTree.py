# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.t_map = collections.Counter()

    def dfsTraverse(self, node):
        if not node: return
        self.t_map[node.val] += 1
        self.dfsTraverse(node.left)
        self.dfsTraverse(node.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.dfsTraverse(root)
        mode = max(self.t_map.values())
        return [k for k, v in self.t_map.items() if v == mode]