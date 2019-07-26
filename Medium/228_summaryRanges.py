class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return nums
        result = []
        left = right = 0
        while right < len(nums) - 1:
            if nums[right + 1] - nums[right] > 1:
                result.append(str(nums[left]) if left == right else str(nums[left]) + "->" + str(nums[right]))
                left = right + 1
            right += 1
        result.append(str(nums[left]) if left == right else str(nums[left]) + "->" + str(nums[right]))
        return result