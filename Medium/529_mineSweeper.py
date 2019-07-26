class Solution:
    # Check the number of adjacent mines around the given position
    def checkAdjacentMines(self, row, col, board):
        mine_count = 0
        for i, j in (row + 1, col), (row + 1, col + 1), (row + 1, col - 1), (row, col + 1), (row, col - 1), (row - 1, col - 1), (row - 1, col + 1), (row - 1, col):
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
                if board[i][j] == 'M':
                    mine_count += 1
        return mine_count

    def reveal(self, row, col, board):
        # Stop recursion
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'E':
            return
        # Check if there is any adjacent mine existed
        n = self.checkAdjacentMines(row, col, board)
        if n > 0:
            # If there is, update the entry to digit
            board[row][col] = str(n)
        else:
            # If there isn't, update the entry to 'B' and keep recursion
            board[row][col] = 'B'
            self.reveal(row + 1, col, board)
            self.reveal(row - 1, col, board)
            self.reveal(row, col + 1, board)
            self.reveal(row, col - 1, board)
            self.reveal(row + 1, col + 1, board)
            self.reveal(row + 1, col - 1, board)
            self.reveal(row - 1, col + 1, board)
            self.reveal(row - 1, col - 1, board)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        clicked = board[click[0]][click[1]]
        if clicked == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            self.reveal(click[0], click[1], board)
        return board

board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

click = [3, 0]
print(Solution().updateBoard(board, click))