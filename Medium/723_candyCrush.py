class Solution:
    # We use negative number to indicate that candies can be eliminated
    # Check whether crash can be made
    def crashExist(self, board):
        exist = False
        # Horizental check - with window shifting of size 3
        for i in range(len(board)):
            for j in range(len(board[i]) - 2):
                if board[i][j] != 0 and abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                    exist = True
        # Vertical check - with window shifting of size 3
        for j in range(len(board[0])):
            for i in range(len(board) - 2):
                if board[i][j] != 0 and abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                    exist = True
        return exist
    # Vertical scan - since the upper candies will drop vertically.
    # Use reversed two pointers way to override negative value with positive value
    # (simulate the dropping mechanism)
    def crashDrop(self, board):
        for j in range(len(board[0])):
            r_index = len(board) - 1
            # Override the eliminated candies with upper candies
            for i in range(len(board) - 1, -1, -1):
                if board[i][j] > 0:
                    board[r_index][j] = board[i][j]
                    r_index -= 1
            # Padding 0s
            for k in range(r_index, -1, -1):
                board[k][j] = 0

    def candyCrush(self, board):
        # Perform until there is no elimination can be made
        while self.crashExist(board):
            self.crashDrop(board)
        return board

board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

Solution().candyCrush(board)
for r in board:
    print(r)