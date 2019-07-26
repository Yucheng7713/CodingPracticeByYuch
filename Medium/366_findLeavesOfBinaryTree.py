# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimLeaves(self, parent, node):
        if not node:
            return []
        if not node.left and not node.right:
            k = node.val
            if parent and parent[1] == 'L': parent[0].left = None
            if parent and parent[1] == 'R': parent[0].right = None
            return [k]
        left_leaves = self.trimLeaves((node, 'L'), node.left)
        right_leaves = self.trimLeaves((node, 'R'), node.right)
        return left_leaves + right_leaves

    def findLeaves(self, root: TreeNode):
        result = []
        if not root: return result
        while root.left != None or root.right != None:
            result.append(self.trimLeaves(None, root))
        result.append([root.val])
        return result

a, b, c, d, e = TreeNode(1), TreeNode(2) ,TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right = b, c
b.left, b.right = d, e
print(Solution().findLeaves(a))

