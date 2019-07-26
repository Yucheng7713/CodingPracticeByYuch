class Solution:
    # Method 1 : Convert BST into inorder array -> a sorted array
    # Then perform the same way as in two sum II -> use two pointers trying to match the target
    def convertTreeInorder(self, node):
        if not node: return []
        return self.convertTreeInorder(node.left) + [node.val] + self.convertTreeInorder(node.right)

    def findTarget_inOrder(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        inorderList = self.convertTreeInorder(root)
        l_index, r_index = 0, len(inorderList) - 1
        while l_index < r_index:
            temp = inorderList[l_index] + inorderList[r_index]
            if temp < k:
                l_index += 1
            elif temp > k:
                r_index -= 1
            else:
                return True
        return False

    # Method 2 : Use hash map

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution:
        def __init__(self):
            self.sum_map = set()

        def findTarget(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: bool
            """
            if not root: return False
            if root.val in self.sum_map:
                return True
            else:
                self.sum_map.add(k - root.val)
            return self.findTarget(root.left, k) or self.findTarget(root.right, k)