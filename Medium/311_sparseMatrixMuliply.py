class Solution:
    def multiply(self, A, B):
        self.sparseMap = dict()
        # Construct the result matrix with right dimension
        result_matrix = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        # Store the non-zero values in the first matrix
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    self.sparseMap[(i, j)] = A[i][j]
        # Traverse the second matrix and see if there exists non zero value
        # If there is B[r2][c2] != 0, check if there exists A[r1][c1] != 0 where c1 == r2
        # If there is, then new matrix[r1][c2] += A[r1][c1] x B[r2][c2]
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] != 0:
                    A = [(key[0], val) for key, val in self.sparseMap.items() if key[1] == i]
                    for a in A:
                        result_matrix[a[0]][j] += a[1] * B[i][j]
        return result_matrix

a = [[1,-5]]
b = [[12],[-1]]

print(Solution().multiply(a, b))