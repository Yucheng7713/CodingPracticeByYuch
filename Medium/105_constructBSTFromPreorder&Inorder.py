# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return
        r_val = preorder.pop(0)
        split = inorder.index(r_val)
        root = TreeNode(r_val)
        if inorder[:split]:
            root.left = self.buildTree(preorder, inorder[:split])
        if inorder[split + 1:]:
            root.right = self.buildTree(preorder, inorder[split + 1:])
        return root

p = [3,9,20,15,7]
i = [9,3,15,20,7]
print(Solution().buildTree(p, i))