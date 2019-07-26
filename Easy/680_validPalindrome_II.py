class Solution:
    def validPalindrome(self, s):
        l_index, r_index = 0, len(s) - 1
        while l_index < r_index:
            if s[l_index] != s[r_index]:
                ld = s[:l_index] + s[l_index + 1:]
                rd = s[:r_index] + s[r_index + 1:]
                if (ld == ld[::-1]) or (rd == rd[::-1]):
                    return True
                return False
            l_index += 1
            r_index -= 1
        return True

s = Solution()
mystr = "abcdef"
print(s.validPalindrome(mystr))