import os
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        else:
            strs.sort(key=len)
            c_prefix = strs[0]
            for i in range(1, len(strs)):
                #Find the longest common prefix with the shortest string
                if c_prefix is "":
                    return ""
                else:
                    c_prefix = os.path.commonprefix([c_prefix, strs[i]])
            return c_prefix

s = Solution()
strings = ["abc"]
print(s.longestCommonPrefix(strings))