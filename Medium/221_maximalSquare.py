class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Brute Force
        max_edge = 0
        rows, cols = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        for i in range(rows):
            for j in range(cols):
                # If the started point = 1 -> start expanding
                if matrix[i][j] == '1':
                    edge = 1
                    flag = True
                    while edge + i < rows and edge + j < cols and flag:
                        for k in range(j, edge + j + 1):
                            if matrix[i + edge][k] == '0':
                                flag = False
                                break
                        for k in range(i, edge + i + 1):
                            if matrix[k][j + edge] == '0':
                                flag = False
                                break
                        if flag: edge += 1
                    if max_edge < edge:
                        max_edge = edge
        return max_edge * max_edge

    def maximalSquare_DP(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        max_side = 0
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i > 0 and j > 0:
                        dp[i][j] = min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]]) + 1
                    else:
                        dp[i][j] = int(matrix[i][j])
                if max_side < dp[i][j]:
                    max_side = dp[i][j]
        return max_side * max_side

mxt = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalSquare_DP(mxt))