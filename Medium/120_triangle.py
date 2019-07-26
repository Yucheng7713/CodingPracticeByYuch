class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle) - 1, 0, -1):
            for j in range(len(triangle[i-1])):
                triangle[i-1][j] = min(triangle[i-1][j] + triangle[i][j], triangle[i-1][j] + triangle[i][j+1])
        return triangle[0][0]

t_array = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(Solution().minimumTotal(t_array))
