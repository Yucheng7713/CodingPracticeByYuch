# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursively traverse the tree and check whether the current path sums up to the value
    # If it does, store the path values
    def dfs(self, root, sum, path, result):
        if not root: return
        if not root.left and not root.right:
            if sum == root.val:
                path += [root.val]
                result += [path]
            return
        # Traverse left and right subtree
        sum -= root.val
        self.dfs(root.left, sum, path + [root.val], result)
        self.dfs(root.right, sum, path + [root.val], result)

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []
        self.dfs(root, sum, [], paths)
        return paths
