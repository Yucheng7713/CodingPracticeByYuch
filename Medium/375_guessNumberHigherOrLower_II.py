class Solution:
    ## Bruce Force Recursion : TLE
    def pickGuess(self, low, high):
        if low >= high: return 0
        min_cost = float('inf')
        for i in range(low, high + 1):
            guranteePickCost = i + max(self.pickGuess(low, i-1), self.pickGuess(i+1, high))
            min_cost = min(min_cost, guranteePickCost)
        return min_cost
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.pickGuess(1, n)

    ## DP
    def getMoneyAmount_DP(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                min_cost = float('inf')
                for pivot in range(start, start + length - 1):
                    worst_cost = pivot + max(dp[start][pivot - 1], dp[pivot + 1][start + length - 1])
                    min_cost = min(min_cost, worst_cost)
                dp[start][start + length - 1] = min_cost
        return dp[1][n]

print(Solution().getMoneyAmount_DP(5))