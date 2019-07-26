class Solution:
    def findStartIndex(self, nums, target):
        low_index, high_index = 0, len(nums) - 1
        while low_index < high_index:
            mid = (low_index + high_index) // 2
            if nums[mid] >= target:
                high_index = mid
            else:
                low_index = mid + 1
        if nums[low_index] == target:
            return low_index
        return -1

    def findEndIndex(self, nums, target):
        low_index, high_index = 0, len(nums) - 1
        while low_index < high_index:
            mid = (low_index + high_index) // 2
            if nums[mid] > target:
                high_index = mid
            else:
                low_index = mid + 1
        if nums[low_index] == target:
            return low_index
        elif nums[low_index - 1] == target:
            return low_index - 1
        return -1

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        result = []
        result.append(self.findStartIndex(nums, target))
        result.append(self.findEndIndex(nums, target))
        return result

s = Solution()
nums = [5,5,7,8,8]
target = 5
print(s.searchRange(nums, target))