# Trivial Dynamic Programming - still very slow
class Solution_I:
    def __init__(self):
        self.coinMap = dict()
    def coinChange(self, coins: List[int], amount: int) -> int:
        # The coin cannot payoff the amount (over paid)
        if amount < 0:
            return -1
        # The amount is paid off
        if amount == 0:
            return 0
        # The amount has been paid -> get the result from the map directly
        if amount in self.coinMap:
            return self.coinMap[amount]
        # Recursively get the fewest number of coins to pay off the amount
        current_min = float('inf')
        for coin in coins:
            temp_min = self.coinChange(coins, amount - coin)
            # If we can pay off 'amount - coin'
            # Record the number as temporary minimum
            if temp_min >= 0 and temp_min < current_min:
                current_min = 1 + temp_min
        # Record the result of the subproblem into the coin map
        self.coinMap[amount] = -1 if current_min == float('inf') else current_min
        return self.coinMap[amount]

class Solution(object):
    # Dynamic Programming - Top-Down
    def minCoinChange(self, coins, known_coins, amount):
        if amount < 0:
            # the coin cannot pay off the amount
            return -1
            # No coin can pay off the amount -> 0
        elif amount == 0:
            return 0
            # If the expecting result exists -> read it from the table
        elif known_coins[amount - 1] != 0:
            return known_coins[amount - 1]
        # Recursively calculate the minimum number of coins for the given amount
        min_coins = float('inf')
        for c in coins:
            res = self.minCoinChange(coins, known_coins, amount - c)
            # If the optimal solution for subproblem "amount - c" is found
            if res >= 0 and res < min_coins:
                # F(S) = min { 1 + F(S - C1), 1 + F(S - C2) ... , 1 + F(S - CN)}
                min_coins = 1 + res
        # There is no optimal solution for subproblem "amount"
        if min_coins == float('inf'):
            # Record table as no solution for the given amount
            known_coins[amount - 1] = -1
        else:
            # Record optimal solution for subproblem "amount"
            known_coins[amount - 1] = min_coins
        return known_coins[amount - 1]

    def coinChange_I(self, coins, amount):
        return self.minCoinChange(coins, [0] * (amount + 1), amount)

    # Dynamic Programming - Bottom-Up
    def coinChange_II(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] + 1 if i - c >= 0 else float('inf') for c in coins])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

    def coinChange_III(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # Iterated filling the dp from 1 to amount
        for i in range(1, amount + 1):
            # Check the minimum number of payoff for amount i
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]

coins = [1,2,5]
amount = 11
print(Solution_I().coinChange(coins, amount))
# print(s.coinChange_III(coins, amount))