class Solution:
    # Divide and Conquer
    # Base case : len(nums) == 1, return nums[0]
    # Subproblem (Divide) : left_sum, right_sum, cross_sum
    # p = (left + right) / 2
    # left_sum = the maximum subarray sum in nums[:p+1]
    # right_sum = the maximum subarray sum in nums[p+1:]
    # cross_sum = the maximum subarray sum which contains both elements in left and right subarray and middle pivot element
    # Merge (Conquer) : max(left_sum, right_sum, cross_sum)


    def crossSum(self, nums, left, p, right) -> int:
        # Since the pivot element is included in the left subarray
        # When counting cross sum, both elements in left and right must be included,
        # If there are only two elements, both elements have to be counted as cross sum according to the requirement
        # e.g. [-1, 2], here the left and pivot element is -1, right element is 2, the cross sum is -1 + 2 = 1
        # so it can be returned directly without further recursion.
        if left + 1 == right:
            return nums[left] + nums[right]
        left_maxsum = right_maxsum = float('-inf')
        current_sum = 0
        # Count the maximum sum in left part
        for i in range(p, left - 1, -1):
            current_sum += nums[i]
            left_maxsum = max(left_maxsum, current_sum)
        current_sum = 0
        # Count the maximum sum in right part
        for i in range(p + 1, right + 1):
            current_sum += nums[i]
            right_maxsum = max(right_maxsum, current_sum)

        # Sum both side to get the maximum contiguous subarray cross sum
        return left_maxsum + right_maxsum

    def maxSubsum(self, nums, left, right) -> int:
        if left == right:
            return nums[left]
        p = (left + right) // 2
        left_sum = self.maxSubsum(nums, left, p)
        right_sum = self.maxSubsum(nums, p + 1, right)
        cross_sum = self.crossSum(nums, left, p, right)

        return max(left_sum, right_sum, cross_sum)

    def maxSubArray_DC(self, nums: List[int]) -> int:
        return self.maxSubsum(nums, 0, len(nums) - 1)

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
