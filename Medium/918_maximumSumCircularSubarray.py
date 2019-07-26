class Solution:
    # Find minimum subarray sum
    def minSubarraySum(self, A):
        current_min = global_min = float('inf')
        for num in A:
            current_min = min(current_min, 0) + num
            global_min = min(global_min, current_min)
        return global_min

    # Find maximum subarray sum
    def maxSubarraySum(self, A):
        current_max = global_max = float('-inf')
        for num in A:
            current_max = max(current_max, 0) + num
            global_max = max(global_max, current_max)
        return global_max

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_subsum = self.maxSubarraySum(A)
        min_subsum = sum(A) - self.minSubarraySum(A)
        # Handling corner case like [-2, -3, -1], if the sum of the array itself is the minimum
        # subarray sum ( the subarray is empty ), then return max_subsum
        return max_subsum if min_subsum == 0 else max(max_subsum, min_subsum)

nums = [3, -1, 2, -1]
print(Solution().maxSubarraySumCircular(nums))