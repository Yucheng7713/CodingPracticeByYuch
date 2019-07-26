class Solution:
    def partitionLabels(self, S: str):
        last = {c : i for i, c in enumerate(S)}
        anchor = cut = 0
        result = []
        for i, c in enumerate(S):
            cut = max(last[c], cut)
            if i == cut:
                result.append(i - anchor + 1)
                anchor = cut = i + 1
        return result

s = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(s))