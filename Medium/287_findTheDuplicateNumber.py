class Solution:
    def findDuplicate(self, nums):
        if len(nums) > 1:
            s_index = nums[0]
            f_index = nums[nums[0]]
            while s_index != f_index:
                s_index = nums[s_index]
                f_index = nums[nums[f_index]]
            print(s_index)
            print(f_index)
            f_index = 0
            while f_index != s_index:
                f_index = nums[f_index]
                s_index = nums[s_index]
            return s_index
        return -1
    # If we are allowed to modified the array
    def findDuplicate_M(selfs, nums):
        if len(nums) > 1:
            index = 0
            while nums[index] > 0:
                index = nums[index] * -1
                if nums[index] < 0:
                    break
                nums[index] *= -1
            return nums[index] * -1
        return -1
s = Solution()
arr = [1,2,3,4,6,4,5]
print(s.findDuplicate(arr))