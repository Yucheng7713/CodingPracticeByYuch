class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, right = 0, 0
        l_dict = dict()
        substr_len, longest_len = 0, 0
        longest_len = 0

        while right < len(s):
            if s[right] not in l_dict:
                l_dict[s[right]] = right
                substr_len += 1
            else:
                substr_len = right - l_dict[s[right]]
                left = l_dict[s[right]] + 1
                l_dict[s[right]] = right
            longest_len = max(substr_len, longest_len)
            right += 1

        return longest_len