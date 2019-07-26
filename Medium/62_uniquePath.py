class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        uni_paths = [[0] * n for i in range(m)]
        for i in range(0, m): uni_paths[i][0] = 1
        for j in range(1, n): uni_paths[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                uni_paths[i][j] = uni_paths[i - 1][j] + uni_paths[i][j - 1]
        return uni_paths[m - 1][n - 1]

print(Solution().uniquePaths(3, 2))