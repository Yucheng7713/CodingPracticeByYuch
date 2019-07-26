class Solution:
    def merge(self, nums1, m, nums2, n):
        index = m
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        nums1.sort()