class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [True] * (n)
        for toggle in range(2, n):
            for j in range(toggle, n + 1, toggle):
                bulbs[j-1] = not bulbs[j-1]
        bulbs[-1] = not bulbs[-1]
        return sum(bulbs)

print(Solution().bulbSwitch(5))