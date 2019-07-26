class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        # Switch the obstacle represented number to -1
        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] *= -1
        # Initialize the uppermost and leftmost number of path to 1
        # until we confront an obstacle
        for i in range(M):
            if obstacleGrid[i][0] == -1:
                break
            else:
                obstacleGrid[i][0] = 1
        for j in range(N):
            if obstacleGrid[0][j] == -1:
                break
            else:
                obstacleGrid[0][j] = 1

        # Calculate the total unique path
        for i in range(1, M):
            for j in range(1, N):
                upper = obstacleGrid[i-1][j] if obstacleGrid[i-1][j] != -1 else 0
                left = obstacleGrid[i][j-1] if obstacleGrid[i][j-1] != -1 else 0
                obstacleGrid[i][j] = upper + left if obstacleGrid[i][j] != -1 else 0
        return obstacleGrid[-1][-1] if obstacleGrid[-1][-1] > 0 else 0