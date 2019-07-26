class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Center expanding method -> Too math
        p_count = 0
        for c in range(2 * len(s) - 1):
            # L and R would be either pointing to the same character or two adjacent characters
            L = c // 2
            R = L + (c % 2)
            # If L and R are the same -> start expanding to see if there is any palindrome
            while L >= 0 and R < len(s) and s[L] == s[R]:
                p_count += 1
                L -= 1
                R += 1
        return p_count

    def countSubstrings_II(self, s: str) -> int:
        def helper(l, r, s):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        numOfStr = 0
        for i in range(len(s)):
            numOfStr += helper(i, i, s)
            numOfStr += helper(i, i+1, s)
        return numOfStr