class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix != []:
            # First sequential line
            res += matrix[0]
            del matrix[0]
            # Vertical right line from top to bottom
            for i in range(0, len(matrix) - 1):
                res.append(matrix[i].pop())
            # Remove empty list element
            matrix = [lst for lst in matrix if lst != []]
            # Bottom line from right to left
            if len(matrix) > 0:
                res += matrix[len(matrix) - 1][::-1]
                del matrix[len(matrix) - 1]
            # Vertical left line from bottom to top
            for j in range(len(matrix) - 1, -1, -1):
                res.append(matrix[j].pop(0))
            # Remove empty list element
            matrix = [lst for lst in matrix if lst != []]
        return res

s = Solution()

matrix_2 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

matrix_2 = [
 [1,2],
 [3,4],
 [5,6]
]

matrix_3 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

matrix_4 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
]

print(s.spiralOrder(matrix_4))