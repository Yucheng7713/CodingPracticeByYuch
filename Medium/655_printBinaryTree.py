class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        # Getting the height of the tree ( starting from 1 )
        def getHeight(node):
            if not node: return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        h = getHeight(root)
        # Construct the 2-D array filling with empty string in advance
        array_tree = [[''] * (2 ** h - 1) for _ in range(h)]

        def printValue(node, level, left, right):
            if not node: return
            mid = (left + right) // 2
            array_tree[level][mid] = str(node.val)
            printValue(node.left, level + 1, left, mid - 1)
            printValue(node.right, level + 1, mid + 1, right)

        printValue(root, 0, 0, 2 ** h - 2)
        return array_tree