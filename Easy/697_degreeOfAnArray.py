from collections import Counter

class Solution:
    # Find the degree of the given array : the maximum occurencce elements
    # Find the minimum subarray which has the same degree as the given array
    # !! There is the case that multiple numbers yield the same degree
    # !! Check the first and last occurence of each element

    # Time complexity : O(n)
    # Space complexity : O(n)
    def findShortestSubArray(self, nums: List[int]) -> int:
        d_list = Counter(nums)
        degree = max(d_list.values())
        ans, first, last = len(nums), {}, {}
        for i, n in enumerate(nums):
            if n not in first:
                first[n] = i
            last[n] = i
        for n, d in d_list.items():
            if d == degree:
                if last[n] - first[n] < ans:
                    ans = last[n] - first[n] + 1
        return ans

d_array = [1, 2, 2, 3, 1]
print(Solution().findShortestSubArray(d_array))
