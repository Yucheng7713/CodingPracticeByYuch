class Solution:
    # Clever way
    def convert_I(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s): return s
        zigZag = [""] * numRows
        k, cursor = 0, -1
        for i, c in enumerate(list(s)):
            if k == 0 or k == numRows - 1:
                cursor *= -1
            zigZag[k] += c
            k += cursor
        return "".join(zigZag)

    # Classic way to solve the problem
    # Time complexity : O(S) which S is the length of the string
    # Space complexity : O(numRows)
    def convert_II(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s
        z_rows = [""] * numRows
        up = False
        i = current_row = 0
        while i < len(s):
            if not up:
                if current_row < numRows:
                    z_rows[current_row] += s[i]
                    current_row += 1
                if current_row > numRows - 1:
                    current_row -= 2
                    up = True
            else:
                if current_row >= 0:
                    z_rows[current_row] += s[i]
                    current_row -= 1
                if current_row < 0:
                    current_row += 2
                    up = False
            i += 1
        return "".join(z_rows)
