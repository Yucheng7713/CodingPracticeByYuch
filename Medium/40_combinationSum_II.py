class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.dfsBacktracking(candidates, target, 0, [], result)
        return result
    def dfsBacktracking(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            if target < nums[i]:
                break
            self.dfsBacktracking(nums, target - nums[i], i + 1, path + [nums[i]], res)