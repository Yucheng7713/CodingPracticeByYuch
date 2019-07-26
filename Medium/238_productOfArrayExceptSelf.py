class Solution(object):
    def productExceptSelf(self, nums):
        result = []
        n = 1
        for i in range(len(nums)):
            result.append(n)
            n = n * nums[i]
        n = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= n
            n *= nums[j]
        return result

nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))