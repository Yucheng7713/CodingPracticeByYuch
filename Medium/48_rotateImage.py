class Solution:
    def rotate(self, matrix):
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row in the matrix
        for lst in matrix:
            lst.reverse()
        return matrix

s = Solution()
arr = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

arr_2 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
print(s.rotate(arr_2))