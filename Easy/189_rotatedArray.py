class Solution:
    def rotate(self, nums, k):
        n = len(nums) - k
        nums[:] = nums[n:] + nums[:n]

    def rotate_2(self, nums, k):



s = Solution()
nums = [1,2]
k = 3
s.rotate(nums, k)
print(nums)