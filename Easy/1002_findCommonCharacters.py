import collections

class Solution:
    def commonChars(self, A):
        common_counter = collections.Counter(A[0])
        for word in A[1:]:
            common_counter &= collections.Counter(word)
        return list(common_counter.elements())

    def commonChars_II(self, A: List[str]) -> List[str]:
        common_list = [float('inf')] * 26
        result = []
        for word in A:
            ch_count = [0] * 26
            for ch in word:
                ch_count[ord(ch) - 97] += 1
            for i in range(26):
                common_list[i] = min(common_list[i], ch_count[i])
        for i, count in enumerate(common_list):
            if count > 0:
                for j in range(count):
                    result.append(chr(i + 97))
        return result

A = ["bella","label","roller"]
print(Solution().commonChars(A))
