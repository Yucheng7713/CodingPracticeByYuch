class Solution:
    # Track all calender days
    # If a day is traveled day or not
    # If it is, then the minimum travel cost for that day ith is : dp[i] =
    # min { yesterday's cost + 1-day-pass cost, 7-days ago's cost + week-pass-cost, a month ago's cost + month-pass-cost }
    # Time complexity : O (N)
    # Space complexity : O (N)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # We only need to track til the last traveled day
        dp = [0] * (max(days) + 1)
        # Function call to avoid index out of range case
        def minCost(day):
            if day <= 0:
                return 0
            return dp[day]
        for i in range(1, len(dp)):
            if i in days:
                dp[i] = min(minCost(i-1)+costs[0], minCost(i-7)+costs[1], minCost(i-30)+costs[2])
            else:
                # For non-traveled day the minimum travel cost is the same as the previous day
                dp[i] = dp[i-1]
        return dp[-1]

days = [1, 4, 6, 7, 8, 20]
costs = [7, 2, 15]
print(Solution().mincostTickets(days, costs))