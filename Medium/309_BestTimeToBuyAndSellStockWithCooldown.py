class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        not_hold, hold, cooldown = 0, float('-inf'), float('-inf')
        for p in prices:
            hold = max(hold, not_hold - p)
            not_hold = max(cooldown, not_hold)
            cooldown = hold + p
        return max(cooldown, not_hold)

