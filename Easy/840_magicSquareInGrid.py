from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j) -> bool:
            a, b, c = grid[i][j], grid[i][j+1], grid[i][j+2]
            d, e, f = grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]
            g, h, i = grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
            sum_r1, sum_r2, sum_r3 = a + b + c, d + e + f, g + h + i
            sum_c1, sum_c2, sum_c3 = a + d + g, b + e + h, c + f + i
            sum_d1, sum_d2 = a + e + i, c + e + g
            d_set = set([a, b, c, d, e, f, g, h, i])
            return sum_r1 == sum_r2 == sum_r3 == sum_c1 == sum_c2 == sum_c3 == sum_d1 == sum_d2 and len(
                d_set) == 9 and all(1 <= n <= 9 for n in list(d_set))

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if isMagic(i, j):
                    result += 1
        return result

grid = [[10,3,5],[1,6,11],[7,9,2]]
print(Solution().numMagicSquaresInside(grid))