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

mylist = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(mylist))