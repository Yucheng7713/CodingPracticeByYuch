class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        s_index = f_index = 0
        min_length = float('inf')
        while f_index < len(nums):
            sub_sum = sum(nums[s_index:f_index + 1])
            if sub_sum < s:
                f_index += 1
            elif sub_sum > s:
                if min_length > f_index - s_index + 1:
                    min_length = f_index - s_index + 1
                s_index += 1
            else:
                if min_length > f_index - s_index + 1:
                    min_length = f_index - s_index + 1
                if f_index < len(nums): f_index += 1
                if s_index < len(nums): s_index += 1
        return [min_length, 0][min_length == float('inf')]

    def minSubArrayLen_II(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        subsum = head = 0
        min_size = float('inf')
        for i in range(len(nums)):
            subsum += nums[i]
            if subsum >= s:
                while subsum >= s:
                    if min_size > i - head + 1:
                        min_size = i - head + 1
                    subsum -= nums[head]
                    head += 1
        return [min_size, 0][min_size == float('inf')]

print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))