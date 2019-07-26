from collections import Counter
class Solution(object):
    # Use Counter -> Extra storage
    def findDuplicates_I(self, nums):
        res = []
        dc = Counter(nums)
        for n in dc:
            if dc[n] == 2:
                res.append(n)
        return res
    # Sort the array -> Time complexity : O(nlogn)
    def findDuplicates_II(self, nums):
        res = []
        nums.sort()
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                res.append(nums[index])
                index += 2
            else:
                index += 1
        return res
    # Legit solution : O(n) linear time without using any extra space
    # Use the input as the hash map -> use the property which 0 <= a[i] <= len(n)
    # Collect all elements that are being pointed twice
    def findDuplicates_III(self, nums):
        res = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return res