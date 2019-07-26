class Solution:
    def backSpacing(self, s):
        result = []
        for l in s:
            if l != '#':
                result.append(l)
            elif l == '#' and result != []:
                result.pop()
        return ''.join(result)
    def backspaceCompare(self, S, T):
        return self.backSpacing(S) == self.backSpacing(T)

s = Solution()
print(s.backSpacing('##ac'))