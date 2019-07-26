class Solution:
    # Wrong implementation
    def getPosition(self, k, n):
        if k % n == 0:
            row = n - k // n
            if row % 2 == 0:
                col = k % n
            else:
                col = n - k % n - 1
        else:
            row = n - k // n - 1
            if row % 2 == 0:
                col = n - k % n
            else:
                col = k % n - 1
        return row, col

    def snakesAndLadders(self, board):
        N = len(board)
        end = N ** 2
        queue = [1]
        dist = { 1 : 0 }
        while queue:
            start = queue.pop(0)
            if start == end:
                return dist[start]
            for nxt in range(start+1, min(end, start+6)+1):
                r, c = self.getPosition(nxt, N)
                if board[r][c] > 0:
                    nxt = board[r][c]
                if nxt not in dist:
                    dist[nxt] = dist[start] + 1
                    queue.append(nxt)
        return -1

class Solution_2:
    def getPosition(self, k, n):
        q, r = divmod(k - 1, n)
        row = n - q - 1
        col = r if row % 2 != n % 2 else n - r - 1
        return row, col
    def snakesAndLadders(self, board):
        N = len(board)
        queue = collections.deque([1])
        dist = { 1 : 0 }
        while queue:
            start = queue.popleft()
            if start == N * N: return dist[start]
            for nxt in range(start+1, min(N*N, start+6)+1):
                r, c = self.getPosition(nxt, N)
                if board[r][c] > 0:
                    nxt = board[r][c]
                if nxt not in dist:
                    dist[nxt] = dist[start] + 1
                    queue.append(nxt)
        return -1

board = [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]
]
board_2 = [[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]
# print(Solution().snakesAndLadders(board_2))
print(Solution().getPosition(20, 5))

