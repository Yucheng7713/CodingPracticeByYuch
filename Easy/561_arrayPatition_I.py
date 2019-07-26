class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        max_sum = 0
        for i in range(0, len(nums), 2):
            max_sum += min(nums[i], nums[i + 1])
        return max_sum

    def arrayPairSum_2(self, nums):
        return sum(sorted(nums)[::2])