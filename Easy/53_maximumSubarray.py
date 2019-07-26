class Solution:
    # Dynamic Programming - Kadane's Algorithm
    # we keep tracking the current maximum subarray sum
    # while tracing down the array
    # and decide to discard the previous subarray sum or
    # start tracking new subarray sum from ith
    def maxSubArray(self, nums) -> int:
        dp = [0] * len(nums)
        res = dp[0] = nums[0]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1], 0) + nums[i]
            res = max(res, dp[i])
        return res

    # Dynamic Programming - Space Optimization
    def maxSubArray_II(self, nums) -> int:
        current_max = global_max = float('-inf')
        for num in nums:
            current_max = max(current_max, 0) + num
            global_max = max(global_max, current_max)
        return global_max

    # Prefix Sum
    def maxSubArray_III(self, nums) -> int:
        current_sum = 0
        res = nums[0]
        current_min = 0
        for num in nums:
            current_sum += num
            res = max(res, current_sum - current_min)
            current_min = min(current_min, current_sum)
        return res

    def minSubArray(self, nums):
        current_min = global_min = float('inf')
        for num in nums:
            current_min = min(current_min, 0) + num
            global_min = min(global_min, current_min)
        return global_min

nums = [-2, -3, -1]
print(Solution().minSubArray(nums))
