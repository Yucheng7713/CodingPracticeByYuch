class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        right = down = -1
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                try:
                    down = grid[i+1][j]
                except:
                    down = -1
                try:
                    right = grid[i][j+1]
                except:
                    right = -1
                if right == -1 and down != -1:
                    grid[i][j] += down
                elif down == -1 and right != -1:
                    grid[i][j] += right
                elif down != -1 and right != -1:
                    grid[i][j] += min(right, down)
        return grid[0][0]