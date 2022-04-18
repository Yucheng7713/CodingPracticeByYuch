class Solution:
    def maxProfit(self, prices):
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))

    def maxProfit_II(selfs, prices):
        max_p= 0
        for i in range(len(prices) - 1):
            max_p += max(prices[i+1] - prices[i], 0)
        return max_p

    def maxProfit_III(self, prices):
        current_min = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < current_min:
                current_min = prices[i]
            if prices[i] - current_min > 0:
                max_profit += prices[i] - current_min
                current_min = prices[i]
        return max_profit