class Solution:
    def knapSack_1(self, n, w, vals, wts):
        dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, w+1):
                if j < wts[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-wts[i-1]] + vals[i-1])
        return dp[-1][-1]
n = 4
w = 10
vals = [10, 40, 30, 50]
wts = [5, 4, 6, 3]
print(Solution().knapSack_1(n, w, vals, wts))