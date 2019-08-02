# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max_BST = 1

        def dfs(node):
            # return (number of nodes, min, max)
            # If there is no node
            if not node:
                return (-1, -1, -1)
            # If it is leaf node
            if not node.left and not node.right:
                return (1, node.val, node.val)

            median = node.val
            left_num, left_min, left_max = dfs(node.left)
            right_num, right_min, right_max = dfs(node.right)

            # If there is any valid BST formed -> calculate their number of nodes
            # Both left and right subtree are valid BSTs
            if left_num > 0 and right_num > 0 and median > left_max and median < right_min:
                self.max_BST = max(self.max_BST, left_num + right_num + 1)
                return (left_num + right_num + 1, left_min, right_max)
            # Only right subtree is a valid BST and left subtree is empty
            if left_num == -1 and right_num > 0 and median < right_min:
                self.max_BST = max(self.max_BST, right_num + 1)
                return (right_num + 1, median, right_max)

            # Only left subtree is a valid BST and right subtree is empty
            if left_num > 0 and right_num == -1 and median > left_max:
                self.max_BST = max(self.max_BST, left_num + 1)
                return (left_num + 1, left_min, median)

            # If there is any subtree that is not a valid BST,
            # return (0, -1, -1)
            return (0, -1, -1)

        dfs(root)
        return self.max_BST