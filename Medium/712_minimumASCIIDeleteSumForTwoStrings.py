class Solution:
    def minimumDeleteSum(self, s1: 'str', s2: 'str') -> 'int':
        # dp[i][j] : answer for s1[i:] and s2[j:]
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        # Initialize dp for cases which one of the string is empty
        for i in range(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i + 1][len(s2)] + ord(s1[i])
        for i in range(len(s2) - 1, -1, -1):
            dp[len(s1)][i] = dp[len(s1)][i + 1] + ord(s2[i])
        # Fill the dp from bottom to top
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j] + ord(s1[i]), dp[i][j + 1] + ord(s2[j]))
        return dp[0][0]