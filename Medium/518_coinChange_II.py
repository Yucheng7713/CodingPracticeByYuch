class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                # If the current amount can be paid by the current coin
                if i >= c:
                    dp[i] += dp[i - c]
        return dp[-1]

    # Optimized version,
    def change_Optimized(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            # We don't need to care the amount which smaller than the current coin
            # Those values will remain unchanged after we start exploring the larger currency coin
            for i in range(c, len(dp)):
                # If the current amount can be paid by the current coin
                dp[i] += dp[i - c]
        return dp[-1]
