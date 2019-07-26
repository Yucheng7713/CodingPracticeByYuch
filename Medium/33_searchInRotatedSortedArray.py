class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        l_index, r_index = 0, len(nums) - 1
        while l_index <= r_index:
            mid = (l_index + r_index) // 2
            if nums[mid] == target:
                return mid
            # the mid is in the second part of the origin list
            if nums[mid] >= nums[l_index]:
                # the ascending part is confirmed as the second part
                if nums[l_index] <= target <= nums[mid]:
                    r_index = mid - 1
                else:
                    l_index = mid + 1
            # the mid is in the first part of the origin list
            else:
                # the ascending part is confirmed as the first part
                if nums[mid] <= target <= nums[r_index]:
                    l_index = mid + 1
                else:
                    r_index = mid - 1
        return -1

s = Solution()
nums, target = [5,6,7,0,1,2,3,4], 6
print(s.search(nums, target))