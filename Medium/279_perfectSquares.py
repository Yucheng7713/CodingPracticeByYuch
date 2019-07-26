class Solution:
    ## Method 1 : DP solution : DP is not accepted in Python
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            tilt = 1
            while i - tilt ** 2 >= 0:
                dp[i] = min(1 + dp[i - tilt ** 2], dp[i])
                tilt += 1
        return dp[-1]

    ## Method 2 : 

print(Solution().numSquares(12))