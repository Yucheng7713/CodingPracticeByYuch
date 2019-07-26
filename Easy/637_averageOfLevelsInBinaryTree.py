# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Calculate average at the same level -> we need to traverse the tree based on level
    # -> BFS
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q, res = [], []
        l_sum = 0
        q.append(root)
        while q:
            l_nodes = len(q)
            for i in range(l_nodes):
                n = q.pop(0)
                l_sum += n.val
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res.append(l_sum / l_nodes)
            l_sum = 0
        return res

t1, t2, t3, t4, t5 = TreeNode(10), TreeNode(5), TreeNode(15), TreeNode(6), TreeNode(20)
t1.left, t1.right = t2, t3
t3.left, t3.right = t4, t5
print(Solution().averageOfLevels(t1))