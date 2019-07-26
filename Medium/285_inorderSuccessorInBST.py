# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTree(self, node):
        if not node: return []
        return self.inorderTree(node.left) + [node.val] + self.inorderTree(node.right)

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        inorderList = self.inorderTree(root)
        s_index = inorderList.index(p.val) + 1
        return None if s_index == len(inorderList) else inorderList[s_index]