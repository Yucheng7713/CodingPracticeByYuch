class Solution:
    def maxProfit(self, prices):
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))

    def maxProfit_II(selfs, prices):
        max_p= 0
        for i in range(len(prices) - 1):
            max_p += max(prices[i+1] - prices[i], 0)
        return max_p