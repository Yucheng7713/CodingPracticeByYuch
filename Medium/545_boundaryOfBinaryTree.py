# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leftBoundary(self, node, path):
        if not node:
            return
        path.append(node.val)
        if node.left:
            self.leftBoundary(node.left, path)
        else:
            self.leftBoundary(node.right, path)

    def rightBoundary(self, node, path):
        if not node:
            return
        path.append(node.val)
        if node.right:
            self.rightBoundary(node.right, path)
        else:
            self.rightBoundary(node.left, path)

    def leavesOfBinaryTree(self, node, leaves):
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.val)
            return
        self.leavesOfBinaryTree(node.left, leaves)
        self.leavesOfBinaryTree(node.right, leaves)

    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        if not root.left and not root.right: return [root.val]
        left_b, right_b, leaves = [], [], []
        if not root.left:
            left_b = [root.val]
        else:
            self.leftBoundary(root, left_b)
        self.leavesOfBinaryTree(root, leaves)
        if not root.right:
            right_b = [root.val]
        else:
            self.rightBoundary(root, right_b)
        if left_b and left_b[0] == root.val:
            left_b.pop(0)
        if left_b and left_b[-1] == leaves[0]:
            leaves.pop(0)
        if leaves and leaves[-1] == right_b[-1]:
            right_b.pop()
        return [root.val] + left_b + leaves + right_b[::-1][:-1]