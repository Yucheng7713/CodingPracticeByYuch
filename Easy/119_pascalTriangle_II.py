class Solution:
    def getRow(self, rowIndex):
        p_row = [1]
        if rowIndex == 0:
            return p_row
        for i in range(rowIndex):
            p_row = list(map(lambda x, y: x + y, p_row + [0], [0] + p_row))
        return p_row

    # Run 30% faster than using map function
    def getRow_II(self, rowIndex):
        p_row = [1]
        if rowIndex == 0:
            return p_row
        for i in range(rowIndex):
            p_row = [x + y for x, y in zip([0] + p_row, p_row + [0])]
        return p_row

s = Solution()
print(s.getRow(3))