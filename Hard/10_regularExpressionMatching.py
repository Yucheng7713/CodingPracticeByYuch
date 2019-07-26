class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-2]
        for j in range(m):
            for k in range(n):
                if s[j] == p[k] or p[k] == '.':
                    dp[j+1][k+1] = dp[j][k]
                elif p[k] == '*':
                    dp[j + 1][k + 1] = dp[j + 1][k - 1]
                    if s[j] == p[k-1] or p[k-1] == '.':
                        dp[j+1][k+1] = dp[j+1][k+1] or dp[j][k+1]
        return dp[-1][-1]

s = "aaa"
p = "ab*a*c*a"
print(Solution().isMatch(s, p))