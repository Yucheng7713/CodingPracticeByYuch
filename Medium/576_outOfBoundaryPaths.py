from functools import lru_cache

class Solution:
    # DFS with LRU cache
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        @lru_cache(None)
        def dfs(i, j, k):
            if k < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            tmp = 0
            for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                tmp += dfs(r, c, k-1)
            return tmp % (10**9 + 7)
        return dfs(i, j, N)

    # DP, dp[(i, j, k)] = the number of paths out of the grid from (i, j) with at most k steps
    def findPaths_DP(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = collections.defaultdict(int)
        MOD = 10 ** 9 + 7
        def helper(i, j, k):
            # If the path has been visited
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            # If the position is in the grid
            if 0 <= i < m and 0 <= j < n:
                # If the steps has been used up -> no further move can be made
                # No path out of the grid
                if k == 0:
                    dp[(i, j, k)] = 0
                    return 0
                else:
                    tmp = 0
                    for r, c in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1):
                        tmp += helper(r, c, k - 1)
                    dp[(i, j, k)] = tmp % MOD
                    return dp[(i, j, k)]
            # If the position is out of the grid -> A path is found!
            else:
                dp[(i, j, k)] = 1
                return 1

        return helper(i, j, N)

print(Solution().findPaths(1, 3, 3, 0, 1))