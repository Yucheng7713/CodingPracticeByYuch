class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print(nums)
        print(nums[::2])
        half = len(nums[::2])
        print(nums[:half][::-1])
        print(nums[half:][::-1])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

n_list = [1,5,1,1,6,4]
Solution().wiggleSort(n_list)
print(n_list)