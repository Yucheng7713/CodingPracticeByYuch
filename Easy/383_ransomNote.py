import collections

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_counter = collections.Counter(list(ransomNote))
        m_counter = collections.Counter(list(magazine))
        for l in r_counter.keys():
            if r_counter[l] > m_counter[l]:
                return False
        return True

print(Solution().canConstruct("a", "b"))