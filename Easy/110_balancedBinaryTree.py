class Solution:
    def isBalanced(self, root):
        if root == None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(
            self.heightAtNode(root.left) - self.heightAtNode(root.right)) <= 1

    def heightAtNode(self, node):
        n_h = 0
        if node == None:
            return n_h
        else:
            return 1 + max(self.heightAtNode(node.left), self.heightAtNode(node.right))

    def isBalanced_II(self, root):

        def dfsCheck(root):
            if root is None:
                return False
            left = dfsCheck(root.left)
            right = dfsCheck(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfsCheck(root) != -1


