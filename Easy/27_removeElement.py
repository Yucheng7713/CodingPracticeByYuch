class Solution(object):
    def removeElement_I(self, nums, val):
        bak = 0
        lnums = len(nums)
        for i in range(lnums):
            if nums[i] != val:
                nums[i-bak] = nums[i]
            else:
                bak +=1
        return lnums - bak

    def removeElement_II(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            nums[slow] = nums[fast]
            if nums[slow] != val:
                slow += 1
        return slow

nums = [0,1,2,2,3,0,4,2]
s = Solution()
print(s.removeElement_2(nums, 2))

