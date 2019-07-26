class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

    def containsDuplicate_2(self, nums):
        n = 1
        for num in nums:
            if num in nums[n:]:
                return False
            n += 1
        return True