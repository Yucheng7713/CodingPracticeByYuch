class Solution:
    def lengthOfLongestSubstring(self):
        s_index = max_len = 0
        str_map = dict()
        for f_index in range(len(s)):
            # If the letter s[f_index] has already been seen ( repeated )
            if s[f_index] in str_map and s_index <= str_map[s[f_index]]:
                s_index = str_map[s[f_index]] + 1
            # Update its seen index
            str_map[s[f_index]] = f_index
            # Update the longest length of substring
            max_len = max(max_len, f_index - s_index + 1)
        return max_len


s = Solution()
string = "abcdefeghiqjkl"
print(s.lengthOfLongestSubstring(string))