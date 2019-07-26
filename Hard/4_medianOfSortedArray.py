class Solution:
    # The time complexity has to be in O(log(m + n))
    # The first intuitive thought will be merging two sorted list then finding the median
    # By doing so, the time complexity will be O(m + n) and so does the space complexity
    # But that way the sorted property of two arrays won't be leverged.

    def findMedianSortedArrays_I(self, nums1, nums2):
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        minA, maxA, B_len = 0, m, (m + n + 1) // 2
        isOdd = ((m + n) % 2 == 1)

        while minA <= maxA:
            i = (minA + maxA) // 2
            j = B_len - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                maxA = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                minA = i + 1
            else:
                if i == 0:
                    left_max = nums2[j - 1]
                elif j == 0:
                    left_max = nums1[i - 1]
                else:
                    left_max = max(nums1[i - 1], nums2[j - 1])

                if isOdd:
                    return left_max

                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])
                return (left_max + right_min) / 2


    def findMedianSortedArrays_II(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        min_i, max_i = 0, m
        halve_len = (m + n + 1) // 2
        # Indicate whether the merged array would be even or odd
        isOdd = ((m + n) % 2 == 1)

        left_max = right_min = 0

        while min_i <= max_i:
            # Assign i and j partitions
            i = (min_i + max_i) // 2
            j = halve_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # means nums1[i] is too small -> increase i
                # the goal is to make nums2[j - 1] <= nums1[i]
                min_i = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # means nums1[i] is too large -> decrease i
                # the goal is to make nums1[i - 1] <= nums2[j]
                max_i = i - 1
            else:
                # a valid partition (i) has been found

                # Edge case handling for i = 0 or j = 0
                if i == 0:
                    left_max = nums2[j - 1]
                elif j == 0:
                    left_max = nums1[i - 1]
                else:
                    left_max = max(nums1[i - 1], nums2[j - 1])

                # If the total number of elements is odd
                # simply return the maximum element at the left
                if isOdd:
                    return left_max

                # Edge case handling for i = m or j = n
                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])

                return (left_max + right_min) // 2

# n1 = [1, 3, 8, 9, 15]
# n2 = [7, 11, 18, 19, 21, 25]
n1 = [1, 3]
n2 = [2]
print(Solution().findMedianSortedArrays_II(n1, n2))