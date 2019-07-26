class Solution:
    def firstUniqChar(self, s):
        c_dict = {}
        non_unique = set()
        first_unique = -1
        for c in s:
            c_dict[c] = c_dict.get(c, 0) + 1
            if c_dict[c] > 1:
                non_unique.add(c)
        for s_index in range(len(s)):
            if s[s_index] not in non_unique:
                first_unique = s_index
                break
        return first_unique

    def firstUniqChar_B(self, s):
        uniqueSet = []
        letterSet = "abcdefghijklmnopqrstuvwxyz"
        for c in letterSet:
            if s.count(c) == 1:
                uniqueSet.append(s.index(c))
        if len(uniqueSet) > 0:
            return min(uniqueSet)
        return -1


s = Solution()
str = "ccbbf"
print(s.firstUniqChar(str))