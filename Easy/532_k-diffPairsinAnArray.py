class Solution:
    # Two pointers method
    def findPairs_I(self, nums: List[int], k: int) -> int:
        ans = 0
        if len(nums) < 2: return ans
        nums.sort()
        i = j = 0
        while i < len(nums) and j < len(nums):
            diff = nums[j] - nums[i]
            if i == j or diff < k:
                j += 1
            elif diff > k:
                i += 1
            else:
                ans += 1
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
        return ans

    # Use Counter
    def findPairs_II(self, nums: List[int], k: int) -> int:
        count_list = collections.Counter(nums)
        ans = 0
        for i in count_list:
            if (k == 0 and count_list[i] > 1) or (k > 0 and i + k in count_list):
                ans += 1
        return ans

    # Use Hashmap
    def findPairs_III(self, nums: List[int], k: int) -> int:
        d_map = dict()
        pair_count = 0
        seen = set()
        for n in sorted(nums):
            if n in d_map:
                if (n, d_map[n]) not in seen:
                    pair_count += 1
                    seen.add((n, d_map[n]))
                    seen.add((d_map[n], n))
            d_map[n + k] = n
        return pair_count

    # Differential cases between k > 0 and k == 0
    def findPairs_III(self, nums: List[int], k: int) -> int:
        if k > 0:
            return len(set(nums) & set([n + k for n in nums]))
        elif k == 0:
            p_counter = collections.Counter(nums)
            return len([p for p in p_counter if p_counter[p] > 1])
        else:
            return 0
