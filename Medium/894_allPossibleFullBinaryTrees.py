# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        # If N = 1, there is only one node
        if N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        allFBTs = []
        for numOfX in range(1, N, 2):
            for left in self.allPossibleFBT(numOfX):
                for right in self.allPossibleFBT(N - numOfX - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    allFBTs.append(root)
        return allFBTs