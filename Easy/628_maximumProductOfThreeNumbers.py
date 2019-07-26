class Solution(object):
    # There can only be two cases :
    # 1. 2 negative number * 1 positive number
    # 2. 3 positive number
    def maximumProduct_I(self, nums):
        if len(nums) == 3:
            return reduce(lambda x, y: x * y, nums, 1)
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])