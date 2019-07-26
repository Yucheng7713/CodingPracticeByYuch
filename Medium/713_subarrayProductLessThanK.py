class Solution:
    def numSubarrayProductLessThanK(self, nums: 'List[int]', k: 'int') -> 'int':
        start = end = 0
        prod, res = 1, 0
        for end in range(len(nums)):
            while start <= end and prod * nums[end] >= k:
                prod /= nums[start]
                start += 1
            if start > end:
                prod = 1
            else:
                prod *= nums[end]
                res += (end - start + 1)
        return res