from DataStructure.Tree import Tree
from DataStructure.Tree import TreeNode

class Solution:
    # Compute the height of the tree from the root
    # Since the tree will be a complete binary tree, we will go all the way down to
    # left subtree to seek for the maxiamum depth
    def heightOfTree(self, root):
        if not root: return -1
        return 1 + self.heightOfTree(root.left)

    def countNodes(self, root):
        # Get the height started from the root
        h = self.heightOfTree(root)
        # None case
        if h < 0: return 0
        # If the right subtree is equally to h - 1 :
        # By the property of complete binary tree, we can ensure that the left subtree
        # must be a perfect binary tree, otherwise the height of right subtree will be
        # smaller than h - 1
        if self.heightOfTree(root.right) == h - 1:
            # The number of nodes in left perfect complete binary tree ( 2^h - 1 ) +
            # 1 ( the root ) + countNodes(root.right) ( since we are not sure whether
            # the right subtree is perfect complete or not, we need to recursively traverse it
            return (1 << h) + self.countNodes(root.right)
        # We can not sure if the left subtree is perfect complete or not, but at least we know
        # that the right subtree is a perfect complete which height is 1 smaller than the root's
        else:
            # The number of nodes in right perfect complete binary tree (2^(h - 1) - 1 +
            # 1 ( the root ) + countNodes(root.left)
            return (1 << h - 1) + self.countNodes(root.left)

bst = Tree().constructTree([1,2,4,5,3,6],[4,2,5,1,6,3])
print(Solution().countNodes(bst))
