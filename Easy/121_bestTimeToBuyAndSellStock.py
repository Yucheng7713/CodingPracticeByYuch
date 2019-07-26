class Solution:
    def maxProfit(self, prices):
        min_price, max_profit = float('inf'), 0
        for p in prices:
            # If a new minimum is found, update it
            if p < min_price:
                min_price = p
            # Update the maximum profit we can acquire at ith
            # ( Possible with the updated minimum price )
            if p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit

s = Solution()
stocks = [7,6,4,3,1]
print(s.maxProfit(stocks))