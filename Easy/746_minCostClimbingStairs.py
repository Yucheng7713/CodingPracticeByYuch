class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost += [0]
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return dp[-1]

stairs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
stairs_2 = [0, 1, 1, 0]
stairs_3 = [10, 15, 20]
print(Solution().minCostClimbingStairs(stairs))