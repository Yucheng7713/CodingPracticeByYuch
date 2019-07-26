class Solution:
    def __init__(self):
        self.d_map = dict()
        self.result = []
    def recordDuplicateSubtrees(self, root):
        # For ensuring the unique serialization for each unique structure of tree
        if not root: return "#"
        str_tree = str(root.val) + self.recordDuplicateSubtrees(root.left) + self.recordDuplicateSubtrees(root.right)
        if self.d_map.get(str_tree) == 1:
            self.result.append(root)
        self.d_map[str_tree] = self.d_map.get(str_tree, 0) + 1
        return str_tree
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.recordDuplicateSubtrees(root)
        return self.result