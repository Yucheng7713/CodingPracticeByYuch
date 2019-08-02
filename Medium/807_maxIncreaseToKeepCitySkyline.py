class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # Find skyline
        m, n = len(grid), len(grid[0])
        result = 0
        top_bottom_skyline = []
        left_right_skyline = [max(row) for row in grid]

        for c in range(n):
            max_col = float('-inf')
            for r in range(m):
                max_col = max(max_col, grid[r][c])
            top_bottom_skyline.append(max_col)

        # Sum up added grids
        for i in range(m):
            for j in range(n):
                result += min(top_bottom_skyline[j], left_right_skyline[i]) - grid[i][j]
        return result