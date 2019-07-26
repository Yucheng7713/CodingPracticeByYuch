from collections import Counter
from collections import defaultdict

class Solution:
    # Brute Force -> TLE
    # Take too much time on checking whether s's window contains all t's characters
    def minWindow_I(self, s: str, t: str) -> str:

        if not t or not s or len(t) > len(s): return ""
        t_wordcount = Counter(t)
        # Iterate hash tables -> Take too much time here!!!
        def desiredWindow(window_str):
            w_wordcount = Counter(window_str)
            return all(w_wordcount[w] >= t_wordcount[w] for w in t_wordcount)
        min_t = ""
        min_len = float('inf')
        L = R = 0
        n = len(s)
        while L <= R:
            # Check whether the current window is desired
            desired = desiredWindow(s[L:R + 1])
            # If it is, check if it is the new minimum
            if desired:
                if len(s[L:R + 1]) < min_len:
                    min_len = len(s[L:R + 1])
                    min_t = s[L:R + 1]
                # Update -> contract at the left
                L += 1
            else:
                if R < n:
                    # Update -> expand at the right
                    R += 1
                else:
                    # If R has already reached to the end
                    # contract at the left
                    L += 1
        return min_t

    def minWindow_II(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n * m == 0 or n < m: return ""

        dict_t, dict_window = Counter(t), defaultdict(int)
        # We use these two indicators to check whether the current window is desired or not
        required, contained = len(dict_t), 0

        min_len = float('inf')
        min_l, min_r, l = 0, 0, 0

        for r in range(n):
            expanded_char = s[r]
            dict_window[expanded_char] += 1
            # Only when the expanded character is in t and the number of occurence is the same :
            if expanded_char in dict_t and dict_t[expanded_char] == dict_window[expanded_char]:
                contained += 1
            # If the state is desired, check and update then start contracting until
            # it is no longer desired.
            while l <= r and required == contained:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_l, min_r = l, r
                contracted_char = s[l]
                dict_window[contracted_char] -= 1
                # If the contracted character is one of the desired characters
                # Update the desired state
                if contracted_char in dict_t and dict_t[contracted_char] > dict_window[contracted_char]:
                    contained -= 1
                l += 1
        return "" if min_len == float('inf') else s[min_l:min_r + 1]



s, t = "bbaac", "aba"
print(Solution().minWindow_II(s, t))