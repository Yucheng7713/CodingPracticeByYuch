class Solution:
    # DFS - Search the 'O' regions in which attach to boundaries
    # Mark them as 'V'
    # Then the rest part will remain as the isolated part
    def dfs(self, row, col, board):
        if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1 or board[row][col] != 'O':
            return
        board[row][col] = 'V'
        self.dfs(row + 1, col, board)
        self.dfs(row - 1, col, board)
        self.dfs(row, col + 1, board)
        self.dfs(row, col - 1, board)

    def solve_DFS(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            M, N = len(board), len(board[0])
            # Left and right boundary
            for col in range(N):
                if board[0][col] == 'O':
                    self.dfs(0, col, board)
                if board[M - 1][col] == 'O':
                    self.dfs(M - 1, col, board)
            # Upper and lower boundary
            for row in range(M):
                if board[row][0] == 'O':
                    self.dfs(row, 0, board)
                if board[row][N - 1] == 'O':
                    self.dfs(row, N - 1, board)
            # Update the marked region : 'V' -> 'O', the rest -> 'X'
            for i in range(M):
                for j in range(N):
                    board[i][j] = "XO"[board[i][j] == 'V']

    # BFS - Search the 'O' regions in which attach to boundaries
    # Starting from the boundary entris
    def solve_BFS(self, board):
        if board and board[0]:
            M, N = len(board), len(board[0])
            queue = []
            for row in range(M):
                if board[row][0] == 'O':
                    queue.append((row, 0))
                if board[row][N - 1] == 'O':
                    queue.append((row, N - 1))
            for col in range(N):
                if board[0][col] == 'O':
                    queue.append((0, col))
                if board[M - 1][col] == 'O':
                    queue.append((M - 1, col))
            while queue:
                i, j = queue.pop(0)
                if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == 'O':
                    board[i][j] = 'V'
                    queue.append((i+1, j))
                    queue.append((i-1, j))
                    queue.append((i, j+1))
                    queue.append((i, j-1))
            for row in range(M):
                for col in range(N):
                    board[row][col] = "XO"[board[row][col] == 'V']


board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
Solution().solve_BFS(board)
print(board)

