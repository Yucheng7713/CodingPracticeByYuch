from typing import List

class Solution:
    # DFS - check from destination to each cell
    # Time complexity : O (mn)
    # Space complexity : O (mn)
    def pacificAtlantic_DFS(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        if not matrix: return result
        m, n = len(matrix), len(matrix[0])
        dirts = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # Table for checking if each cell can reach pacific / atlantic ocean
        pacific_visited = [[False for _ in range(n)] for _ in range(m)]
        atlantic_visited = [[False for _ in range(n)] for _ in range(m)]

        def dfsWaterFlow(i, j, visited):
            visited[i][j] = True
            for dirt in dirts:
                x, y = i + dirt[0], j + dirt[1]
                # If the moved position is invalid or it has already been visited or water cannot flow from
                # that cell to the current cell. ( which the current cell is higher )
                if x < 0 or x > m - 1 or y < 0 or y > n - 1 or visited[x][y] or matrix[x][y] < matrix[i][j]:
                    continue
                dfsWaterFlow(x, y, visited)

        # Start from cells which are adjacent to ocean
        for i in range(m):
            dfsWaterFlow(i, 0, pacific_visited)
            dfsWaterFlow(i, n - 1, atlantic_visited)
        for j in range(n):
            dfsWaterFlow(0, j, pacific_visited)
            dfsWaterFlow(m - 1, j, atlantic_visited)

        # If a cell can both reach from pacific and atlantic ocean, then
        # push the cell into the result.
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i, j])

        return result

    # BFS - check from destination to each cell
    def pacificAtlantic_BFS(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        if not matrix: return result
        m, n = len(matrix), len(matrix[0])
        dirts = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pacific_visited, atlantic_visited = set(), set()

        # Initialize reachable cells which are adjacent to pacific / atlantic ocean
        for r in range(m):
            pacific_visited.add((r, 0))
            atlantic_visited.add((r, n - 1))
        for c in range(n):
            pacific_visited.add((0, c))
            atlantic_visited.add((m - 1, c))

        # BFS method
        def bfsWaterFlow(visited):
            q = collections.deque(visited)
            while q:
                r, c = q.popleft()
                for dirt in dirts:
                    x, y = r + dirt[0], c + dirt[1]
                    # If the move is valid (in the matrix) and it hasn't been visited yet plus water can flow from
                    # that cell (x, y) to the current cell (r, c)
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and matrix[x][y] >= matrix[r][c]:
                        q.append((x, y))
                        visited.add((x, y))
            return visited

        return list(bfsWaterFlow(pacific_visited) & bfsWaterFlow(atlantic_visited))

matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(Solution().pacificAtlantic(matrix))