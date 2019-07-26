import bisect

class Solution:
    # Sort element by their absolute difference with the target
    # Then get the first kth elements
    # The elements with same absolute
    def findClosestElements(self, arr, k: int, x: int):
        arr.sort(key=lambda c: abs(x - c))
        print(arr)
        return sorted(arr[:k])

    # Binary search with 2 pointers
    def findClosestElements_II(self, arr, k: int, x: int):
        # target element is out of the array at the left side
        # return the first kth elements
        if x < arr[0]:
            return arr[:k]
        # if the target element is out of the array at the right side
        # return the last kth elements
        if x > arr[-1]:
            return arr[-k:]
        # Find the index of the target element
        index = bisect.bisect(arr, x)
        # Find the index of the leftmost possible element
        low = max(0, index - k - 1)
        # Find the index of the rightmost possible element
        high = min(len(arr) - 1, index + k - 1)
        # Shrink the window [low:high] until it size reduces to kth
        while high - low + 1 > k:
            if abs(arr[low] - x) <= abs(arr[high] - x):
                high -= 1
            else:
                low += 1
        return arr[low:high + 1]

nums = [1,2,3,4,5]
k = 4
x = 3
print(Solution().findClosestElements_II(nums, k, x))