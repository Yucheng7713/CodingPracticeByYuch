class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = count = 0
        if len(nums) == 0:
            return 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                count = 0
            if count >= max_count:
                max_count = count
        return max_count