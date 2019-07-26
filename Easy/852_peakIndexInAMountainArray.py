class Solution:
    # Linear scan
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        peak = None
        for i, h in enumerate(A):
            if i > 0 and h < A[i-1]:
                peak = i-1
                break
        return peak

    # Binary search
    def peakIndexInMountainArray_II(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] < A[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l
