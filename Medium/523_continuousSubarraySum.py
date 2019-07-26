class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_map = dict()
        # Map : key -> reminder, value -> index
        # Initial state : 0 -> -1
        sum_map[0] = -1
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            # Avoid mod 0 cases
            if k != 0:
                # We only care about the reminder
                current_sum %= k
            # If the reminder have never occured -> record it
            if current_sum not in sum_map:
                sum_map[current_sum] = i
            # else check the last occur index by accessing the hash map
            # if the length (difference) between them > 1, that means
            # we find a subarray sum which equals to k x n with a length > 1
            else:
                if i - sum_map[current_sum] > 1:
                    return True
        return False

