class Solution:
    def findDisappearedNumbers(self, nums):
        d_nums = [0] * len(nums)
        for i in range(len(nums)):
            d_nums[nums[i] - 1] = 1
        return [k+1 for k in range(len(d_nums)) if d_nums[k] == 0]

s = Solution()
arr = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(arr))