class Solution:
    # 暴力解法 -> 找出每個 subarray 並計算其總和，之後看是否 = k
    # Time complexity : O(n^3)
    # Space complexity : O(1)

    def subarraySum_bruteForce(self, nums, k):
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                if sum(nums[i:j]) == k:
                    res += 1
        return res

    # 利用 prefix sum 來省去最內層的 sum -> O(n)
    # 用一 sum array 來儲存到 index i 之前的總和 : sum[i]
    # 若要求 subarray[i:j]總和：sum[j+1] - sum[i]
    # Time complexity : O(n^2)
    # Space complexity : O(n)

    def subarraySum_prefixSum(self, nums, k):
        res = 0
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        for start in range(len(nums)):
            for end in range(start+1, len(nums) + 1):
                if prefix_sum[end] - prefix_sum[start] == k:
                    res += 1
        return res

    # This method can be achieved by using constant space
    # Time complexity : O(n^2)
    # Space complexity : O(n)

    def subarraySum_prefixSum_withoutSpace(self, nums, k):
        res = 0
        for start in range(len(nums)):
            prefix_sum = 0
            for end in range(start, len(nums)):
                prefix_sum += nums[end]
                if prefix_sum == k:
                    res += 1
        return res

    # Use hash map
    # Since we only seek for the number of subarray sum
    # We search for current_sum - k
    # Since the elements between current_sum and current_sum - k will sum up to k
    # 有幾次 current_sum - k, 就有幾個 subarray sum = k
    def subarraySum_hashMap(self, nums: List[int], k: int) -> int:
        sum_map = collections.defaultdict(int)
        ans = current_sum = 0
        sum_map[0] = 1
        for n in nums:
            # Keep accumulating current sum
            current_sum += n
            # If there is current_sum - k subarray exist
            if current_sum - k in sum_map:
                # We add and record the number of new subarrays between
                # current_sum - k ( there might be many current_sum - k subarray in previous array )
                # and current_sum
                ans += sum_map[current_sum - k]
            # Record the new occurance of current_sum
            sum_map[current_sum] += 1
        return ans



print(Solution().subarraySum_hashMap([1,1,1], 2))