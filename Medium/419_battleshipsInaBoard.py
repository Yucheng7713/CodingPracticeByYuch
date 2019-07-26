# Regular DFS
class Solution_1:
    def dfs(self, row, col, board):
        if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]) and board[row][col] == 'X':
            board[row][col] = 'O'
            self.dfs(row + 1, col, board)
            self.dfs(row - 1, col, board)
            self.dfs(row, col + 1, board)
            self.dfs(row, col - 1, board)

    def countBattleships(self, board):
        m, n = len(board), len(board[0])
        ships = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    self.dfs(i, j, board)
                    ships += 1
        return ships

# Simply count the first 'X' according to the pattern of battleship
# pattern 1:
# X....X ( the first 'X' will be counted only if its upper and left neighbor is not 'X')
# pattern 2 :
# X ( the first 'X' will be counted only if its upper and left neighbor is not 'X' )
# .
# .
# .
# X
class Solution_2:
    def countBattleships(self, board):
        m, n = len(board), len(board[0])
        ships = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] != 'X') and (j == 0 or board[i][j-1] != 'X'):
                    ships += 1
        return ships

board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(Solution().countBattleships(board))