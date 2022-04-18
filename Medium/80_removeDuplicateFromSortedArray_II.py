from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        for n in nums:
            # Move i index only when :
            # 1. For special cases : i = 0, i = 1 which there is no preceding 2 elements
            # 2. There is no third duplicate appeared
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
            # Otherwise the i index will stop at the third duplicate and wait for being overwrited
        return i

    def removeDuplicates_I(self, nums: List[int]) -> int:
        d_count, anchor = 1, 0
        for i in range(len(nums)):
            nums[anchor] = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                d_count += 1
            else:
                d_count = 1
            if d_count <= 2:
                anchor += 1
        return anchor

mylist = [1,1,1,2,2,3]
print(Solution().removeDuplicates(mylist))