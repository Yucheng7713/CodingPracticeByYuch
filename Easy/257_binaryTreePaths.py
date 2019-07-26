# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfsTraverse(root, path, results):
            # Avoid exploring null cases
            if not root:
                return
            # If we reach a leaf node
            elif not root.left and not root.right:
                results.append(path + str(root.val))
                return
            dfsTraverse(root.left, path + str(root.val) + "->", results)
            dfsTraverse(root.right, path + str(root.val) + "->", results)
        paths = []
        dfsTraverse(root,"", paths)
        return paths