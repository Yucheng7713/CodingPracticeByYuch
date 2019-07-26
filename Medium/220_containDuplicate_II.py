class Solution:
    # Brute Force : TLE
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if len(nums) < 2: return False
        for l in range(len(nums)):
            for r in range(l + 1, len(nums)):
                if abs(l - r) <= k:
                    if abs(nums[l] - nums[r]) <= t:
                        return True
        return False

    # Bucket sort
    def containsNearbyAlmostDuplicate_II(self, nums, k: int, t: int) -> bool:
        if k < 0 or t < 0: return False
        bucket = dict()
        bucket_width = t + 1
        for i in range(len(nums)):
            label = nums[i] // bucket_width
            if label in bucket:
                return True
            if label - 1 in bucket and abs(nums[i] - bucket[label - 1]) < bucket_width:
                return True
            if label + 1 in bucket and abs(nums[i] - bucket[label + 1]) < bucket_width:
                return True
            bucket[label] = nums[i]
            if i >= k:
                del bucket[nums[i - k] // bucket_width]
        return False


nums = [1, 5, 9, 1, 5, 9]
k = 2
t = 3
print(Solution().containsNearbyAlmostDuplicate(nums, k, t))