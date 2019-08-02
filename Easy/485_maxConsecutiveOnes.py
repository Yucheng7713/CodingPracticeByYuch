class Solution:
    def findMaxConsecutiveOnes_I(self, nums):
        max_count, count = float('-inf'), 0
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

    # Two Pointers method
    def findMaxConsecutiveOnes_II(self, nums: List[int]) -> int:
        r = l = 0
        max_length = float('-inf')
        while r < len(nums):
            if nums[r] == 1:
                max_length = max(r - l + 1, max_length)
                r += 1
            else:
                l = r
                l, r = l + 1, r + 1
        return 0 if max_length == float('-inf') else max_length