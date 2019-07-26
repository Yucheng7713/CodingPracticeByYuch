class Solution:
    # BFS brute force : perform BFS at each entry which equals to INF
    # TLE
    def wallsAndGates_I(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        def shortestDistance(row, col):
            visited = []
            r_queue = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            distance = 0
            while r_queue:
                len_q = len(r_queue)
                for k in range(len_q):
                    i, j = r_queue.pop(0)
                    visited += [(i, j)]
                    if i >= 0 and i < len(rooms) and j >= 0 and j < len(rooms[0]):
                        if rooms[i][j] > 0:
                            if (i+1, j) not in visited : r_queue.append((i + 1, j))
                            if (i-1, j) not in visited : r_queue.append((i - 1, j))
                            if (i, j+1) not in visited : r_queue.append((i, j + 1))
                            if (i, j-1) not in visited : r_queue.append((i, j - 1))
                        elif rooms[i][j] == 0:
                            return distance + 1
                distance += 1
            return INF

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == INF:
                    # BFS find shortest distance starting from (i, j)
                    rooms[i][j] = shortestDistance(i, j)

    # BFS search starting at the gate, assign encountered rooms with distance
    def wallsAndGates_II(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        def shortestDistance(row, col):
            r_queue = [(row, col)]
            visited = []
            while r_queue:
                q_len = len(r_queue)
                for k in range(q_len):
                    i, j = r_queue.pop(0)
                    visited += [(i, j)]
                    for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if r >= 0 and r < len(rooms) and c >= 0 and c < len(rooms[0]) and rooms[r][c] > 0 and (r, c) not in visited:
                            rooms[r][c] = min(rooms[r][c], rooms[i][j] + 1)
                            r_queue.append((r, c))

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    # BFS find shortest distance starting from (i, j)
                    shortestDistance(i, j)

    # Concise BFS :
    # We don't need to worry if an updated entry get overwrited by later BFS
    # Whichever update an entry first, the updated value is exactly the shorter one
    # Cuz it reaches first.
    def wallsAndGates_III(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        if rooms and rooms[0]:
            INF = 2 ** 31 - 1
            M, N = len(rooms), len(rooms[0])
            r_queue = []
            r_queue = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
            # for i in range(M):
            #     for j in range(N):
            #         if rooms[i][j] == 0:
            #             r_queue += [(i, j)]
            for i, j in r_queue:
                for r, c in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= r < M and 0 <= c < N and rooms[r][c] == INF:
                        rooms[r][c] = rooms[i][j] + 1
                        r_queue += [(r, c)]

wg = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Solution().wallsAndGates_III(wg)
print(wg)


