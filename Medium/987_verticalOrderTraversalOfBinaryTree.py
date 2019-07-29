from collections import defaultdict
from functools import cmp_to_key

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Hash Map + DFS
    # Time complexity : O (VlogV) - It's bounded by sorting parts
    # Space complexity : O (V) - Since the number of edges of binary tree will always be one less than the number of nodes
    # E = V - 1, so space complexity = O (V + E) = O (V + V - 1) = O (2V - 1) ~= O (V)
    def verticalTraversal(self, root):
        pos_list, result = [], []
        horizental_map = defaultdict(list)

        def dfsTraverse(node, x, y):
            if not node:
                return
            pos_list.append((x, y, node.val))
            dfsTraverse(node.left, x - 1, y - 1)
            dfsTraverse(node.right, x + 1, y - 1)

        dfsTraverse(root, 0, 0)
        pos_list = sorted(pos_list, key=lambda x: (x[0], -x[1], x[2]))
        for pos_node in pos_list:
            horizental_map[pos_node[0]].append(pos_node[2])
        for node_list in horizental_map.values():
            result.append(node_list)
        return result

a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
a.left, a.right = b, c
c.left, c.right = d, e

print(Solution().verticalTraversal(a))