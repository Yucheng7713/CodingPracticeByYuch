import sys

class Solution:
    def findFirstDescend(self, nums):
        # if nums == None:
        #     return None
        # if len(nums) == 1:
        #     return nums[0]
        result = -1
        firstDes = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if firstDes > nums[i]:
                result = i
                break
            firstDes = nums[i]
        if result == -1:
            return None
        return result

    def findMinMaximum(self, nums, start_index):
        minVal, result = sys.maxsize, -1
        for i in range(start_index + 1, len(nums)):
            if nums[i] > nums[start_index] and minVal >= nums[i]:
                minVal = nums[i]
                result = i
        if result == -1:
            return None
        return result

    def nextPermutation(self, nums):
        if len(nums) > 1:
            l_index = self.findFirstDescend(nums)
            print("Left substitution : " + str(l_index))
            if l_index == None:
                nums.reverse()
            else:
                r_index = self.findMinMaximum(nums, l_index)
                print("Right substitution : " + str(r_index))
                nums[l_index], nums[r_index] = nums[r_index], nums[l_index]
                nums[l_index + 1:] = nums[l_index + 1:][::-1]
        print(nums)

    def nextPermutation_2(selfs, nums):


s = Solution()
nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
nums_1 = [2,3,1,3,3]
s.nextPermutation(nums_1)
