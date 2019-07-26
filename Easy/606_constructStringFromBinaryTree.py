class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ""
        elif not t.left and not t.right: return str(t.val)
        l_str, r_str = '(' + self.tree2str(t.left) + ')', '(' + self.tree2str(t.right) + ')'
        if r_str == "()":
            r_str = ""
        t_str = str(t.val) + l_str + r_str
        return t_str