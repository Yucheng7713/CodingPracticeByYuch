class Solution:
    def maxAreaOfIsland(self, grid):
        def i_area(r, c):
            # if r or c out of the range of the grid and has been visited and == 0 -> return 0
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]):
                grid[r][c] = 0
                return (1 + i_area(r - 1, c) + i_area(r + 1, c) + i_area(r, c - 1) + i_area(r, c + 1))
            return 0
        areas = [i_area(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col]]
        print(areas)
        return max(areas) if areas else 0

    def dfs(self, row, col, grid):
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] != 1:
            return 0
        grid[row][col] = -1
        return 1 + self.dfs(row + 1, col, grid) + self.dfs(row - 1, col, grid) \
               + self.dfs(row, col + 1, grid) + self.dfs(row, col - 1, grid)

    def maxAreaOfIsland_II(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(i, j, grid))
        return max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

s = Solution()
print(s.maxAreaOfIsland(grid))