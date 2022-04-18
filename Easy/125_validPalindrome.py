class Solution:
    def isPalindrome_I(self, s: str) -> bool:
        if not s: return True
        new_s = ''.join([c.lower() for c in s if c.isalnum()])
        mid = len(new_s) // 2
        print(len(new_s))
        left = mid - 1
        right = mid if len(new_s) % 2 == 0 else mid + 1
        while left >= 0 and right < len(new_s):
            if new_s[left] != new_s[right]:
                return False
            left -= 1
            right += 1
        return True

    def isPalindrome_II(self, s):
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]

str = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome_I(str))
