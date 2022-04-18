class Solution:
    def moveZeroes(self, nums):
        l_index, f_index = 0, 0
        while f_index < len(nums):
            if nums[f_index] != 0:
                temp = nums[f_index]
                nums[f_index] = nums[l_index]
                nums[l_index] = temp
                l_index += 1
            f_index += 1
        return nums

    def moveZeroes_II(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            if nums[j] != 0:
                j += 1

    def moveZeroes_III(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        # Remove 0 elements
        s = f = 0
        while f < len(nums):
            nums[s] = nums[f]
            if nums[f] != 0:
                s += 1
            f += 1
        # The rest elements remain 0
        for i in range(s, len(nums)):
            nums[i] = 0

s = Solution()
nums = [0,0,0,0,1,2,0]
print(s.moveZeroes(nums))
