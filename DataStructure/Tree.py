# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def constructTree(self, preorder, inorder):
        if not preorder or not inorder: return None
        r = preorder.pop(0)
        root = TreeNode(r)
        r_index = inorder.index(r)
        root.left = self.constructTree(preorder, inorder[:r_index])
        root.right = self.constructTree(preorder, inorder[r_index + 1:])
        return root

# Way to call module : from DataStructure.Tree import *


