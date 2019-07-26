class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backTracking(nums):
            if not nums:
                return [[]]
            subset = []
            for i in range(len(nums)):
                k = self.subsetsWithDup(nums[i+1:])
                for s in k:
                    if s not in subset:
                        subset.append(s)
                    new_s = [nums[i]]
                    new_s += s
                    if new_s not in subset:
                        subset.append(new_s)
            return subset
        return backTracking(sorted(nums))
nums = [1,2,2]
print(Solution().subsetsWithDup(nums))