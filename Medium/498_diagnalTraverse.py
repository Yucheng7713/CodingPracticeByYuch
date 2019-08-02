import collections
from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        result = []
        diagnal_map = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                diagnal_map[i+j+1].append(matrix[i][j])
        for k, d_list in diagnal_map.items():
            if k % 2 == 1:
                result += d_list[::-1]
            else:
                result += d_list
        return result

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
matrix_2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
print(Solution().findDiagonalOrder(matrix_2))