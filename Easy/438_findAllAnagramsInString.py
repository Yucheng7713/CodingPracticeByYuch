from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        s_counter = Counter(s[:len(p) - 1])
        p_counter = Counter(p)
        a_indices = []

        for i in range(len(p) - 1, len(s)):
            s_count[s[i]] += 1
            if s_count == p_count:
                a_indices.append(i - len(p) + 1)
            s_count[s[i - len(p) + 1]] -= 1
            if s_count[s[i - len(p) + 1]] == 0:
                del s_count[s[i - len(p) + 1]]
        return a_indices

sol = Solution()
print(sol.findAnagrams(s, p))