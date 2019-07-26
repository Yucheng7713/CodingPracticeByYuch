class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        else:
            anchor = 0
            for i in range(1, len(nums)):
                if nums[anchor] != nums[i]:
                    nums[anchor + 1] = nums[i]
                    anchor += 1
            print(nums[0:anchor + 1])
            return len(nums[0:anchor + 1])

    def removeDuplicates_II(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        left = 0
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1

s = Solution()
numbers = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(numbers))