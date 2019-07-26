class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10: return []
        dna_map = {}
        for i in range(len(s) - 9):
            dna_str = s[i:i+10]
            dna_map[dna_str] = dna_map.get(dna_str, 0) + 1
        return [k for k, v in dna_map.items() if v > 1]

dna = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(Solution().findRepeatedDnaSequences(dna))