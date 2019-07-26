class Solution:
    def binarySearch(self, head, tail, nums, k):
        while head != tail:
            m = (head + tail) // 2
            # if nums[m] < k : k will be inserted at the right part of the array
            if nums[m] < k:
                head = m + 1
            else:
                tail = m
        return head
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            # Binary search : find the position for inserting x
            i_index = self.binarySearch(0, size, dp, x)
            tails[i_index] = x
            if i_index == size:
                size = i_index + 1
        return size

mylist = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(mylist))