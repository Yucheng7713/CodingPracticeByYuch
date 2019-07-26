class Solution(object):
    def rob(self, nums):
        rob = not_rob = 0
        for n in nums:
            temp = rob
            rob = max(not_rob + n, rob)
            not_rob = temp
        return rob

    def rob_2(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]
s = Solution()
nums = [2,7,9,3,1]
print(s.rob(nums))