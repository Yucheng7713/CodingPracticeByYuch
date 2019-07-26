class Solution:

    def permute_short(self, nums):
        return [[n] + p for i, n in enumerate(nums) for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]
    def permute(self, nums):
        result = []
        self.backTracking(nums, [], result)
        return result
    def backTracking(self, nums, path, result):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            self.backTracking(nums[:i] + nums[i+1:], path + [nums[i]], result)

s = Solution()
nums = [2,3]
print(nums[:1])
print(nums[2:])
