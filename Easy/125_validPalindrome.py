class Solution:
    def isPalindrome(self, s):
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]

s = Solution()
str = "A man, a plan, a canal: Panama"
print(s.isPalindrome(str))

myStr = "ABDEFGC"
print(myStr.lower())