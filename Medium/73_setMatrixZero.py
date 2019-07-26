class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        new_matrix = [[float('inf')] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    new_matrix[i] = [0] * n
                    for k in range(m):
                        new_matrix[k][j] = 0
                elif new_matrix[i][j] != 0:
                    new_matrix[i][j] = matrix[i][j]
        return new_matrix
        # If modify in place
        # for i in range(m):
        #     for j in range(n):
        #         matrix[i][j] = new_matrix[i][j]

mxt = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(Solution().setZeroes(mxt))

