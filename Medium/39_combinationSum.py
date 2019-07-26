class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        self.dfsBacktracking(candidates, target, 0, [], result)
        return result
    def dfsBacktracking(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfsBacktracking(nums, target - nums[i], i, path + [nums[i]], res)