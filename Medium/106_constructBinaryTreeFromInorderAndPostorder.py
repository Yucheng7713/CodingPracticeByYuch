# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postordfajr or not inorder: return None
        r = postorder.pop()
        r_index = inorder.index(r)
        root = TreeNode(r)
        root.right = self.buildTree(inorder[r_index+1:], postorder)
        root.left = self.buildTree(inorder[:r_index], postorder)
        return root