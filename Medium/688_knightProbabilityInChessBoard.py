from functools import lru_cache

class Solution:
    # Dynamic Programming - Basic
    # Find the probability at each position on the board at each step
    # Final goal : sum of the probabilities of each position on the board at each step
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        # Check wheter the given position (r, c) is on board
        def inBoard(r, c):
            return 0 <= r < N and 0 <= c < N
        # dp0 : for probabilites at step k
        dp0 = [[0 for _ in range(N)] for _ in range(N)]
        # The initial position where the knight piece is placed
        dp0[r][c] = 1
        for k in range(1, K + 1):
            # dp1 : for probabilites at step k + 1
            dp1 = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    prob = 0
                    for dr, dc in (1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1):
                        new_r, new_c = i + dr, j + dc
                        if inBoard(new_r, new_c):
                            prob += dp0[new_r][new_c] / 8.0
                    dp1[i][j] = prob
            dp0 = dp1
        # the probability sum on the board will be the probability which the knight remains on the board
        return sum(map(sum, dp0))

    # DFS
    def knightProbability_II(self, N: int, K: int, r: int, c: int) -> float:
        @lru_cache(None)
        def dfs(K, r, c, p):
            if K == 0:
                return p
            total_p = 0
            for i, j in (r + 1, c + 2), (r - 1, c + 2), (r + 1, c - 2), (r - 1, c - 2), (r + 2, c + 1), (
                r + 2, c - 1), (r - 2, c + 1), (r - 2, c - 1):
                if 0 <= i < N and 0 <= j < N:
                    total_p += dfs(K - 1, i, j, p * 0.125)
            return total_p

        return dfs(K, r, c, 1)

print(Solution().knightProbability(3, 2, 0, 0))