# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return
        r_index = nums.index(max(nums))
        root = TreeNode(nums[r_index])
        root.left = self.constructMaximumBinaryTree(nums[:r_index])
        root.right = self.constructMaximumBinaryTree(nums[r_index+1:])
        return root