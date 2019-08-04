from typing import List

class Solution:
    # Method 1: Dynamic Programming
    # Time complexity : O(n * sum)
    # Space complexity : O(n * sum)
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        target = n // 2
        # If the sum is not even, there is no way to divide them into two parition with equal subsum
        if n % 2 == 1:
            return False
        # If there is any single number which equals to half of the sum, we find a partition right away
        # The number itself + the rest numbers
        if target in nums:
            return True
        # 2D array
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]

        # DP initialization
        for i in range(len(dp)):
            dp[i][0] = True
        for j in range(1, len(dp[0])):
            dp[0][j] = False


        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i - 1][j]
                # If the rest capacity can take the next element
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]

    def canPartition_II(self, nums: List[int]) -> bool:
        # Easy check
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        memo = dict()

        # Recursively find if subset exists
        def isSubsetSum(nums, start, target, memo):
            if target in memo:
                return memo[target]
            if target == 0:
                memo[target] = True
            else:
                memo[target] = False
                # Check whether the target can be summed up by nums[start] + nums[start+1] + ... + nums[-1]
                # start = 0 and nums[start] = 1
                # [1, 5, 11, 5] -> find sum = 11
                # [5, 11, 5] -> find sum = 10 (include nums[start] already)
                # .....
                # if there is no sum can be found by including nums[start] ( but such case will never happen )
                # then start + 1
                # [5, 11, 5] -> find sum = 11
                if target > 0:
                    for i in range(start, len(nums)):
                        if isSubsetSum(nums, i + 1, target - nums[i], memo):
                            memo[target] = True
                            break
            return memo[target]

        return isSubsetSum(nums, 0, target, memo)

nums = [1, 5, 11, 5]
print(Solution().canPartition_II(nums))