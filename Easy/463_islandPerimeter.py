class Solution:
    def surroundZero(self, island):
        new_island = [[0 for _ in range(len(island[0])+2)] for _ in range(len(island)+2)]
        for i in range(len(island)):
            for j in range(len(island[0])):
                if island[i][j] == 1:
                    new_island[i + 1][j + 1] = 1
        return new_island
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i_length = 0
        new_grid = self.surroundZero(grid)
        for i in range(1, len(new_grid) - 1):
            for j in range(1, len(new_grid[0]) - 1):
                if new_grid[i][j] == 1:
                    numOfZero = (new_grid[i-1][j] == 0) + (new_grid[i][j-1] == 0) + (new_grid[i+1][j] == 0) + (new_grid[i][j+1] == 0)
                    i_length += numOfZero
        return i_length

    def islandPerimeter_II(self, grid):
        island = [[0 for _ in range(len(grid[0]) + 2)] for _ in range(len(grid) + 2)]
        for i in range(1, len(island) - 2):
            for j in range(1, len(island[0]) - 2):
                island[i][j] = grid[i][j]
        i_p = 0
        for i in range(len(island)):
            for j in range(len(island[0])):
                if island[i][j] == 1:
                    numOfZeros = sum(
                        [1 for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if island[r][c] == 0])
                    i_p += numOfZeros
        return i_p

    def islandPerimeter_III(self, grid):
        i_p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    i_p += 4
                    if j > 0 and grid[i][j - 1] == 1:
                        i_p -= 2
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        i_p -= 2
        return i_p

i = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print(Solution().islandPerimeter_II(i))