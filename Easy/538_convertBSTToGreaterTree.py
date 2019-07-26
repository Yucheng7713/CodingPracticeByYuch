class Solution:
    def __init__(self):
        # use a variable to keep track of the sum
        self.g_sum = 0
    # we just need to traverse the entire tree and update nodes' value
    # don't need to modify its structure -> don't need to assign the return tree node
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            # visit the right subtree first -> the greater part
            self.convertBST(root.right)
            # update root's value
            self.g_sum += root.val
            root.val = self.g_sum
            self.convertBST(root.left)
        return root
