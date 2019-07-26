class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if matrix and matrix[0]:
            # Treat the 2D matrix as sorted list
            # Given index ith, the corresponding element in the matrix is
            # matrix[i // numOfColumn][i % numOfColumn]
            m, n = len(matrix), len(matrix[0])
            l, r = 0, m * n - 1
            while l < r:
                mid = (l + r - 1) // 2
                # We just need to care referring the right number from
                # the matrix
                mid_num = matrix[mid // n][mid % n]
                if target > mid_num:
                    l = mid + 1
                else:
                    r = mid
            return matrix[r // n][r % n] == target
        return False


