from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_count = Counter(s1)
        s2_count = Counter(s2[:k])
        if all(s1_count[c] == s2_count[c] for c in s1_count):
            return True
        for i in range(1, len(s2) - k + 1):
            rm_char, new_char = s2[i-1], s2[i + k - 1]
            if s2_count[rm_char] > 0:
                s2_count[rm_char] -= 1
            s2_count[new_char] += 1
            if all(s1_count[c] == s2_count[c] for c in s1_count):
                return True
        return False

s1 = "a"
s2 = "ab"
print(Solution().checkInclusion(s1, s2))