class Solution:
    def sameTree(self, t1, t2):
        if not t1 and not t2: return True
        elif (not t1 and t2) or (not t2 and t1): return False
        return t1.val == t2.val and self.sameTree(t1.left, t2.left) and self.sameTree(t1.right, t2.right)
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s: return False
        elif self.sameTree(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)