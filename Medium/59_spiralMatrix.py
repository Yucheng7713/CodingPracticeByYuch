class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mxt = [[0] * n for i in range(n)]
        s, t = 1, n * n
        Dir = {'R':'D', 'D':'L', 'L':'U', 'U':'R'}
        left_bound = top_bound = 0
        right_bound = bottom_bound = n - 1
        d = 'R'
        while s <= t:
            if d == 'R':
                for i in range(left_bound, right_bound + 1):
                    mxt[top_bound][i] = s
                    s += 1
                top_bound += 1
            elif d == 'D':
                for i in range(top_bound, bottom_bound + 1):
                    mxt[i][right_bound] = s
                    s += 1
                right_bound -= 1
            elif d == 'L':
                for i in range(right_bound, left_bound - 1, -1):
                    mxt[bottom_bound][i] = s
                    s += 1
                bottom_bound -= 1
            elif d == 'U':
                for i in range(bottom_bound, top_bound - 1, -1):
                    mxt[i][left_bound] = s
                    s += 1
                left_bound += 1
            d = Dir[d]
        return mxt

print(Solution().generateMatrix(3))