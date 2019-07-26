class Solution:
    def isValidSudoku(self, board):
        return self.isValidRow(board) and self.isValidColumn(board) and self.isValidSubBoard(board)

    def isValidRow(self, board):
        for row in board:
            if not self.isUnitValid(row):
                return False
        return True

    def isValidColumn(self, board):
        for column in zip(*board):
            if not self.isUnitValid(column):
                return False
        return True

    def isValidSubBoard(self, board):
        for i in range(0, len(board) - 2, 3):
            for j in range(0, len(board[i]) - 2, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isUnitValid(square):
                    return False
        return True

    def isUnitValid(self, unit):
        unit = [i for i in unit if i != "."]
        return len(unit) == len(set(unit))