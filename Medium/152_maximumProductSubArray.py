import sys
from functools import reduce

class Solution:
    # Bruce Force - Try out all lengths and their started index
    def maxProduct_I(self, nums):
        max_p = - sys.maxsize + 1
        for i in range(1, len(nums) + 1):
            for j in range(len(nums) - i + 1):
                if max_p < reduce(lambda x, y: x * y, nums[j: j + i], 1):
                    max_p = reduce(lambda x, y: x * y, nums[j: j + i], 1)
        return max_p
    # Clever way - O(n)

    def maxProduct_II(self, nums):
        local_min = local_max = max_p = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                local_min, local_max = local_max, local_min
            local_max = max(nums[i], local_max * nums[i])
            local_min = min(nums[i], local_min * nums[i])
            max_p = max(max_p, local_max)
        return max_p

    def minProduct(self, nums):
        local_min = local_max = min_p = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                local_min, local_max = local_max, local_min
            local_max = max(nums[i], local_max * nums[i])
            local_min = min(nums[i], local_min * nums[i])
            min_p = min(min_p, local_min)
        return min_p

    def maxSum(self, nums):
        local_max = max_sum = nums[0]

        for i in range(1, len(nums)):
            local_max = max(nums[i], local_max + nums[i])
            max_sum = max(max_sum, local_max)
        return max_sum

s = Solution()
arr = [2,3,-7,4,-1,5]
print(s.maxSum(arr))