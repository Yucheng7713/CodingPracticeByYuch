class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        p_str = str.split(' ')
        if len(pattern) != len(p_str): return False
        pattern_map = dict()
        for i, p in enumerate(list(pattern)):
            if p not in pattern_map:
                if p_str[i] in pattern_map.values(): return False
                pattern_map[p] = p_str[i]
            elif pattern_map[p] != p_str[i]:
                return False
        return True

p, s = "abba", "dog cat cat dog"
print(Solution().wordPattern(p, s))