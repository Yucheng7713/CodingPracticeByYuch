class Solution:
    # DFS - Wrong implementation
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(r, c, dirt, visited, stopped):
            if r < 0 or r > len(maze[0])-1 or c < 0 or c > len(maze)-1 or (r, c) in visited: return
            visited.add((r, c))
            if dirt == 'U':
                if r < 1 or maze[r-1][c] == 1:
                    stopped.add((r, c))
                    dfs(r, c+1, 'R', visited, stopped)
                    dfs(r, c-1, 'L', visited, stopped)
                    dfs(r+1, c, 'D', visited, stopped)
                else:
                    dfs(r-1, c, 'U', visited, stopped)
            elif dirt == 'D':
                if r > len(maze)-2 or maze[r+1][c] == 1:
                    stopped.add((r, c))
                    dfs(r, c+1, 'R', visited, stopped)
                    dfs(r, c-1, 'L', visited, stopped)
                    dfs(r-1, c, 'U', visited, stopped)
                else:
                    dfs(r+1, c, 'D', visited, stopped)
            elif dirt == 'L':
                if c < 1 or maze[r][c-1] == 1:
                    stopped.add((r, c))
                    dfs(r, c+1, 'R', visited, stopped)
                    dfs(r+1, c, 'D', visited, stopped)
                    dfs(r-1, c, 'U', visited, stopped)
                else:
                    dfs(r, c-1, 'L', visited, stopped)
            else:
                if c > len(maze[0])-2 or maze[r][c+1] == 1:
                    stopped.add((r, c))
                    dfs(r, c-1, 'L', visited, stopped)
                    dfs(r+1, c, 'D', visited, stopped)
                    dfs(r-1, c, 'U', visited, stopped)
                else:
                    dfs(r, c+1, 'R', visited, stopped)
        visited = set()
        stopped = set()
        dfs(start[0], start[1], 'U', visited, stopped)
        return (destination[0], destination[1]) in stopped

    def hasPath_DFS(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(r, c, stopped):
            if (r, c) in stopped: return False
            stopped.add((r, c))
            if (destination[0], destination[1]) in stopped: return True
            for i, j in (1, 0), (-1, 0), (0, 1), (0, -1):
                new_r, new_c = r, c
                while 0 <= new_r + i < len(maze) and 0 <= new_c + j < len(maze[0]) and maze[new_r + i][new_c + j] != 1:
                    new_r += i
                    new_c += j
                if dfs(new_r, new_c, stopped):
                    return True
            return False
        return dfs(start[0], start[1], set())

    def hasPath_BFS(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = collections.deque([tuple(start)])
        visited = set()
        while queue:
            new_queue = collections.deque()
            while queue:
                r, c = queue.popleft()
                if (r, c) == tuple(destination): return True
                for i, j in (1, 0), (-1, 0), (0, 1), (0, -1):
                    new_r, new_c = r, c
                    while 0 <= new_r + i < len(maze) and 0 <= new_c + j < len(maze[0]) and maze[new_r + i][new_c + j] != 1:
                        new_r += i
                        new_c += j
                    if (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        new_queue.enque((new_r, new_c))
            queue = new_queue
        return False

# maze = [
#     [0,0,1,0,0],
#     [0,0,0,0,0],
#     [0,0,0,1,0],
#     [1,1,0,1,1],
#     [0,0,0,0,0]
# ]
# start = [0,4]
# destination = [3,2]
maze = [
    [0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1],
    [0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,1,0,0,0,1],
    [0,0,0,0,1,0,0]]
start = [0,0]
destination =  [8,6]
print(Solution().hasPath(maze, start, destination))
