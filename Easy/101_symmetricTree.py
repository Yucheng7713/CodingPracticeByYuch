# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    def isMirror(self, leftSubTree, rightSubTree):
        if leftSubTree and rightSubTree:
            return (leftSubTree.val == rightSubTree.val) and self.isMirror(leftSubTree.left, rightSubTree.right) and self.isMirror(leftSubTree.right, rightSubTree.left)
        return leftSubTree is rightSubTree