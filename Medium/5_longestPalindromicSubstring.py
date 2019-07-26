class Solution:
    # Brute Force method (TLE)
    # Checking if the given string is palindromic or not
    def palindromeCheck(self, s):
        mid = len(s) // 2
        right = mid
        left = mid if len(s) % 2 == 1 else mid - 1
        N = mid + 1 if len(s) % 2 == 1 else mid
        for i in range(N):
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
        return True

    def longestPalindrome_I(self, s: str) -> str:
        longest_palstr = ""
        max_len = 0
        # Try out all possible substring and find the longest one that is palindromic
        for i in range(len(s)):
            for j in range(len(s)):
                sub_str = s[i:j]
                if self.palindromeCheck(sub_str) and len(sub_str) > max_len:
                    longest_palstr = sub_str
                    max_len = len(sub_str)
        return longest_palstr

    # Dynamic Programming - Improved version of Brute Force
    def longestPalindrome_DP_I(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        max_len = 1
        longest_palin = ""
        # Prefilled the base cases for
        # 1. P(i, i) = True
        # 2. P(i, i+1) = True
        for i in range(len(s)):
            dp[i][i] = True
            longest_palin = s[i]
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                max_len = 2
                longest_palin = s[i:i+2]
        # Filled the dp map diagnally, the goal is to find the longest palindrome
        # P(0, len(s) which is the rightmost top.
        # If
        for i in range(2, len(s)):
            r = 0
            for j in range(i, len(s)):
                dp[r][j] = dp[r + 1][j - 1] and s[r] == s[j]
                if dp[r][j] and len(s[r:j+1]) > max_len:
                    longest_palin = s[r:j+1]
                    max_len = len(longest_palin)
                r += 1
        return longest_palin

    def longestPalindrome_DP_II(self, s: str) -> str:
        n = len(s)
        if n <= 1: return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        longest_palin = s[0] if len(s) > 0 else ""
        max_len = 0
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest_palin = s[i] * 2
        max_len = len(longest_palin)
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                sub_str = s[i: j + 1]
                if dp[i][j] and len(sub_str) > max_len:
                    longest_palin = sub_str
                    max_len = len(longest_palin)
        return longest_palin

    # Find the longest possible palindrome starting from i and j
    # i and j would either be the same ( odd number length palindrome )
    # or i + 1 = j ( even number length palindrome )
    def palindrome(self, i, j, s):
        # Keep expanding until reaching boundaries or s[i] != s[j]
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        # Return the expanded palindrome string
        return s[i + 1:j]

    def longestPalindrome_III(self, s: str) -> str:
        max_len = 0
        longest_palin = ""
        for i in range(len(s)):
            # Odd length case
            odd_palin = self.palindrome(i, i, s)
            if len(odd_palin) > max_len:
                longest_palin = odd_palin
                max_len = len(odd_palin)
            # Even length case
            even_palin = self.palindrome(i, i + 1, s)
            if len(even_palin) > max_len:
                longest_palin = even_palin
                max_len = len(even_palin)
        return longest_palin

p_str = "abcdba"
print(Solution().palindromeCheck(p_str))