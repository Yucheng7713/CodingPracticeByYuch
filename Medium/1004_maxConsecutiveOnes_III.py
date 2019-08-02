from collections import Counter
class Solution:
    # Method 1 : Sliding window + tracking number of 0's and 1's
    def longestOnes_I(self, A: List[int], K: int) -> int:
        l = r = 0
        max_length = float('-inf')
        binary_count = Counter()
        while r < len(A):
            binary_count[A[r]] += 1
            while binary_count[0] > K:
                binary_count[A[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1
        return 0 if max_length == float('-inf') else max_length

    # Method 1.2 : Use without hash map + For loop
    def longestOnes_II(self, A: List[int], K: int) -> int:
        l = r = 0
        max_length = float('-inf')
        numOfZeros = 0
        for r in range(len(A)):
            if A[r] == 0:
                numOfZeros += 1
            if numOfZeros > K:
                if A[l] == 0:
                    numOfZeros -= 1
                l += 1
            if r - l + 1 > max_length:
                max_length = r - l + 1
        return 0 if max_length == float('-inf') else max_length