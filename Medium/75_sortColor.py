class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c_count = {}
        for n in nums:
            c_count[n] = c_count.get(n,0) + 1
        k = list(c_count.keys())
        k.sort(reverse=True)
        color = k.pop()
        for i in range(len(nums)):
            if c_count[color] > 0:
                nums[i] = color
                c_count[color] -= 1
            if k != [] and c_count[color] == 0:
                color = k.pop()
        return nums

print(Solution().sortColors([2,0,2,1,1,0]))