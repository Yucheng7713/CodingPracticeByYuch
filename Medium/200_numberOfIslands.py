class Solution:
    # Method 1 : Use DFS search at each element
    def dfs(self, grid, row, col):
        # Until we encounter the boundary or an ocean block '0' or a visited block '-1'
        # !! Make sure to place grid[row][col] != '1' at the end otherwise the statement
        # might be examined in advance with invalid row or column
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] != '1':
            return
        # Mark (row, col) as visited
        grid[row][col] = ''
        # Recursively call for the upper, lower, left and right entry
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col - 1)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        numOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # when discover a land block and the land block (i, j) hasn't been visited
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    numOfIslands += 1
        return numOfIslands

i_sland = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','1']
]

s = Solution()
print(s.numIslands(i_sland))