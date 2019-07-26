class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if root == None:
            return []
        treeQueue = []
        sameLevelQueue = []
        results = []
        treeQueue.append(root)
        while treeQueue != []:
            result = []
            while treeQueue != []:
                expNode = treeQueue.pop(0)
                if expNode.left:
                    sameLevelQueue.append(expNode.left)
                if expNode.right:
                    sameLevelQueue.append(expNode.right)
                result.append(expNode.val)
            results = [result] + results
            treeQueue = sameLevelQueue
            sameLevelQueue = []
        return results

a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
a.left, a.right = b, c
c.left, c.right = d, e

s = Solution()
print(s.levelOrderBottom(a))