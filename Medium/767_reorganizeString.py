class Solution:
    def reorganizeString(self, S):
        A, res = [], [None] * len(S)
        n = (len(S) + 1) // 2
        for c, s in sorted((S.count(x), x) for x in set(S)):
            if c > n: return ""
            A.extend(c * s)
        res[::2], res[1::2] = A[len(S)//2:], A[:len(S)//2]
        return "".join(res)

print(Solution().reorganizeString("AAABBB"))