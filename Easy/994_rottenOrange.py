class Solution:
    # BFS traversal - 1.0 ver
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_queue = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_queue.append((i, j))
        time = 0
        while rotten_queue:
            temp_queue = []
            while rotten_queue:
                r, c = rotten_queue.pop(0)
                for i, j in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        temp_queue.append((i, j))
            rotten_queue = temp_queue
            time += 1
        if time > 0: time -= 1
        return time if all(grid[i][j] == 2 or grid[i][j] == 0 for i in range(m) for j in range(n)) else -1

