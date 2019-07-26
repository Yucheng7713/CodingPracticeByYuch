class Solution(object):

    def gameOfLife_I(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        die_to_live, live_to_die = [], []

        def numOfLives(i, j):
            lives_count = 0
            for r, c in (i + 1, j), (i - 1, j), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1), (i, j + 1), (
            i, j - 1), (i - 1, j - 1):
                if 0 <= r < m and 0 <= c < n and board[r][c] == 1:
                    lives_count += 1
            return lives_count

        for i in range(m):
            for j in range(n):
                l_count = numOfLives(i, j)
                if board[i][j] == 1:
                    if l_count < 2 or l_count > 3:
                        live_to_die.append((i, j))
                else:
                    if l_count == 3:
                        die_to_live.append((i, j))

        for r, c in live_to_die:
            board[r][c] = 0
        for r, c in die_to_live:
            board[r][c] = 1

    # Follow-up I : Implement without any extra memory
    # Use different notation to represent the updating statuses
    # Make sure they can still be applied to the rule
    def gameOfLife_II(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
                Do not return anything, modify board in-place instead.
                """
        # 3 : from live to death
        # 2 : from death to live
        m, n = len(board), len(board[0])

        def countLives(r, c):
            adj_pos = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
            count = 0
            for i, j in adj_pos:
                if 0 <= r + i < m and 0 <= c + j < n:
                    count += (board[r + i][c + j] % 2)
            return count

        for i in range(m):
            for j in range(n):
                numOfLives = countLives(i, j)
                # 1 -> 0 if n < 2 or n > 3
                # 0 -> 1 if n == 3
                # 1 -> 1 if n == 2 or n == 3
                if board[i][j] == 0:
                    if numOfLives == 3:
                        board[i][j] = 2
                else:
                    if numOfLives < 2 or numOfLives > 3:
                        board[i][j] = 3

        board = [[ 1 if board[i][j] == 1 or board[i][j] == 2 else 0 for j in range(n)] for i in range(m)]

        print(board)

    # Follow-up II : What if the board is infinitively large?
    # def gameOfLife_III(self, board) -> None:


s = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
s.gameOfLife_II(board)