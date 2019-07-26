from DataStructure.Tree import TreeNode
from DataStructure.Tree import Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left: return root
        leftMost = self.upsideDownBinaryTree(root.left)
        root.left.right = root
        if root.right:
            root.left.left = root.right
        root.left, root.right = None, None
        return leftMost

t = Tree().constructTree([1,2,4,5,3],[4,2,5,1,3])
upside_down_t = Solution().upsideDownBinaryTree(t)
print(upside_down_t)

