class Solution:
    def frequencySort(self, s: str) -> str:
        str_count = sorted(collections.Counter(list(s)).items(), key=lambda x: x[1], reverse=True)
        return "".join([c * freq for c, freq in str_count])