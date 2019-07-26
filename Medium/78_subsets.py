class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, index, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i+1, [nums[i]] + path, res)
        results = []
        nums.sort(reverse=True)
        dfs(nums, 0, [], results)
        return results