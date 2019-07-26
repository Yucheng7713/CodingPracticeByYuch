class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        if nums == []:
            return None
        if nums[0] <= nums[-1]:
            return nums[0]
        while left != right:
            mid = (left + right) // 2
            if nums[mid] < nums[0]:
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                else:
                    right = mid
            else:
                if nums[mid] > nums[mid + 1]:
                    left = mid
                else:
                    return nums[mid]

s = Solution()
arr = []
print(s.findMin(arr))