class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_nums = [1]
        u2, u3, u5 = 2, 3, 5
        i2 = i3 = i5 = 0
        for i in range(n):
            min_ugly = min([u2, u3, u5])
            ugly_nums.append(min_ugly)
            if min_ugly == u2:
                i2 += 1
                u2 = 2 * ugly_nums[i2]
            if min_ugly == u3:
                i3 += 1
                u3 = 3 * ugly_nums[i3]
            if min_ugly == u5:
                i5 += 1
                u5 = 5 * ugly_nums[i5]
        return ugly_nums[-1]

print(Solution().nthUglyNumber(10))