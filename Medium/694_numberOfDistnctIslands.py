class Solution:
    # BFS traversal -> Use traverse path to identify the shape of an island
    # MLE -> Memory limit exceed
    def numDistinctIslands_I(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        s_map = collections.defaultdict(int)
        # BFS traverse
        def BFS(row, col, grid):
            queue = [(row, col)]
            shape = "1"
            for r, c in queue:
                grid[r][c] = 0
                for i, j in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= i < M and 0 <= j < N and grid[i][j] == 1:
                        queue += [(i, j)]
                        shape += '1'
                    else:
                        shape += '0'
            s_map[shape] += 1

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    BFS(i, j, grid)
        return len(s_map.keys())

    # DFS traversal -> Use relative position to identify the shape of an island
    # In each iteration, it's guarantee that the top-leftmost of an island will be
    # visited first, we use this position as the start point regarding as (0, 0)
    # As we traverse the island, we mark each '1' with its relative position.
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        s_map = set()
        # DFS traversal
        def dfs(row, col, pos, rel_pos):
            grid[row][col] = -1
            for dirt in (1, 0), (-1, 0), (0, 1), (0, -1):
                i, j = row + dirt[0], col + dirt[1]
                if 0 <= i < M and 0 <= j < N and grid[i][j] == 1:
                    # Update the new relative position
                    new_rel_pos = rel_pos[0] + dirt[0], rel_pos[1] + dirt[1]
                    # Record the new relative position as a part of the island shape
                    pos += [new_rel_pos]
                    dfs(i, j, pos, new_rel_pos)

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    position = []
                    dfs(i, j, position, (0, 0))
                    # Record the shape of the discovered island
                    s_map.add(tuple(position))
        # Return the number of island genres.
        return len(s_map)
