class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Ending case -> to leaf nodes
        if not root:
            return
        # Swap the left and right child recursively
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root