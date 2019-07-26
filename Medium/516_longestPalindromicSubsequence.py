import sys

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # Base case
        for i in range(len(s)):
            dp[i][i] = 1
        for j in range(1, len(s)):
            k = 0
            for i in range(j, len(s)):
                if s[k] == s[i]:
                    dp[k][i] = dp[k+1][i-1] + 2
                else:
                    dp[k][i] = max(dp[k+1][i], dp[k][i-1])
                k += 1
        return dp[0][-1]

    def longestPalindromeSubseq_DP(self, s: str) -> int:
        n = len(s)
        # If the given string is null or only contain 1 character
        if n <= 1: return n
        # The entire string is a palindrome
        if s == s[::-1]: return len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                # A longer palindrome subsequence is found
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # Choose the one formed the longer palindrome subsequence
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


s = "bbbab"
print(Solution().longestPalindromeSubseq_II(s))