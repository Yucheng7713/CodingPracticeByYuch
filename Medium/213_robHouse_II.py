class Solution:
    def singleRob(self, nums):
        rob = not_rob = 0
        for n in nums:
            temp = rob
            rob = max(not_rob + n, rob)
            not_rob = temp
        return rob

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        rob_first = self.singleRob(nus[:-1])
        rob_last = self.singleRob(nums[1:])
        return max(rob_first, rob_last)

houses = [2]
print(Solution().rob(houses))