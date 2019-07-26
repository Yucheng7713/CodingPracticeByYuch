class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def placeIntoSubset(nums, subsets, target):
            if not nums: return True
            v = nums.pop()
            for i, subsum in enumerate(subsets):
                if v + subsum <= target:
                    subsets[i] += v
                    if placeIntoSubset(nums, subsets, target):
                        return True
                    subsets[i] -= v
                if subsum == 0:
                    break
            nums.append(v)
            return False
        nums.sort()
        target, reminder = divmod(sum(nums), k)
        # If the total sum can't be divided into k subset or
        # there is number which greater than the target
        # Since there is no negative number
        if reminder or nums[-1] > target: return False
        # Reduce the search space - get rid of single number subset
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return placeIntoSubset(nums, [0] * k, target)

nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(Solution().canPartitionKSubsets(nums, k))