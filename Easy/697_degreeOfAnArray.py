from collections import Counter

class Solution:

    def findShortestSubArray(self, nums):
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        print(first)
        print(last)
        d_col = Counter(nums)
        max_degree = max(d_col.values())

        return min(last[i] - first[i] + 1 for i, v in d_col.items() if v == max_degree)

s = Solution()
d_array = [1, 2, 2, 3, 1]
print(s.findShortestSubArray(d_array))
