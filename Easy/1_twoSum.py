class Solution(object):
    def twoSum(self, nums, target):
        sumMap = {}
        for i in range(0, len(nums)):
            if nums[i] in sumMap:
                return [sumMap[nums[i]], i]
            else:
                sumMap[target - nums[i]] = i

s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))

# Classic way : using hash map
