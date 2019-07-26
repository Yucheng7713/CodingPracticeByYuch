class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        if len(nums) > 2:
            n = 1
            while n < len(nums) - 1:
                nums[n], nums[n + 1] = nums[n + 1], nums[n]
                n += 2
    def wiggleSort_II(self, nums):
        """
                :type nums: List[int]
                :rtype: void Do not return anything, modify nums in-place instead.
                """
        for i in range(1, len(nums), 2):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            if i + 1 < len(nums) and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]