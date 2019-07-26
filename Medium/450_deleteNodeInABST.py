# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        # If the deleted node is in the right subtree
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        # If the deleted node is in the left subtree
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # If the deleted node is found -> start deleting and reducing tree
        else:
            # If only right subtree exists, directly connect to it
            if not root.left and root.right: return root.right
            # If only left subtree exists, directly connect to it
            elif not root.right and root.left: return root.left
            # If the deleted node is a leaf node -> directly change it to None
            elif not root.right and not root.left: return None
            # If both left and right subtree exists,
            # substitute the root's value to the maximum value in left subtree
            # then delete the chosen node in the left subtree
            # recursively do above
            else:
                mini_left = root.left
                new_root_val = mini_left.val
                # Find the maximum value in left subtree -> must be in the rightmost
                # subtree
                while mini_left.right:
                    mini_left = mini_left.right
                    new_root_val = mini_left.val
                root.val = new_root_val
                root.left = self.deleteNode(root.left, new_root_val)
        return root