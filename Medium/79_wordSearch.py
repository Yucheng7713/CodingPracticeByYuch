class Solution:
    def dfs(self, board, row, col, word):
        # The word is found and match
        if len(word) == 0:
            return True
        # Out of the board's range
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or word[0] != board[row][col]:
            return False
        f_ch = board[row][col]
        # Block the character for later search
        board[row][col] = '#'
        # Check both horizental and vertical direction
        res = self.dfs(board, row + 1, col, word[1:]) or self.dfs(board, row - 1, col, word[1:]) or self.dfs(board, row, col + 1, word[1:]) or self.dfs(board, row, col - 1, word[1:])
        # Back tracking -> recover the blocked character
        board[row][col] = f_ch
        return res
    def exist(self, board, word):
        if not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Check whether the word exists starting from (i,j)
                if self.dfs(board, i, j, word):
                    return True
        return False