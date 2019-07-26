class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s): return s
        zigZag = [""] * numRows
        k, cursor = 0, -1
        for i, c in enumerate(list(s)):
            if k == 0 or k == numRows - 1:
                cursor *= -1
            zigZag[k] += c
            k += cursor
        return "".join(zigZag)
