class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        hold = -prices[0] if len(prices) > 0 else 0
        not_hold = 0
        for i in range(1, len(prices)):
            hold = max(hold, not_hold - prices[i])
            not_hold = max(not_hold, hold + prices[i] - fee)
        return max(hold, not_hold)

prices = [1, 3, 2, 8, 4, 9]
f = 2
print(Solution().maxProfit(prices, f))