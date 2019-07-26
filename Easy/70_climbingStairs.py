class Solution(object):
    def climbStairs(self, n):
        steps = []
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            steps.append(1)
            steps.append(2)
            for i in range(2, n):
                steps.append(steps[i - 1] + steps[i - 2])
            print(steps)
            return steps[n - 1]



s = Solution()
print(s.climbStairs(10))