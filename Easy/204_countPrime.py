class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        pn = []
        nums = [True] * n
        nums[0] = nums[1] = False
        for i in range(2, n):
            if nums[i]:
                # Record all prime numbers
                pn.append(i)
                time_range = (n - 1)//i + 1
                for j in range(2, time_range):
                    nums[i * j] = False
        print(pn)
        return sum(nums)

s = Solution()
print(s.countPrimes(10))