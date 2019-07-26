class Solution:
    def isIsomorphic(self, s, t):
        r_red = dict()
        red_r = dict()
        for i in range(len(s)):
            if (s[i] in r_red and r_red[s[i]] != t[i]) or (t[i] in red_r and red_r[t[i]] != s[i]):
                return False
            r_red[s[i]] = t[i]
            red_r[t[i]] = s[i]
        return True