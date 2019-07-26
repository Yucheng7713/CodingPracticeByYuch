from collections import deque

class Solution:
    # Brute Force - nested iteration
    # Time complexity : O (KN), Space complexity : O (N - K + 1)
    def maxSlidingWindow_I(self, nums, k: int):
        max_nums = []
        n = len(nums)
        if n * k == 0: return max_nums
        if k == 1: return nums
        for i in range(n - k + 1):
            max_nums.append(max(nums[i:i+k]))
        return max_nums

    # Deque - Scaling window size and keep track of the current maximum + remove all smaller
    # Time complexity : O (N) - each element will only be processed twice - enque and deque
    # Space complexity : O (N) - O (N-k+1) for output, O (k) for deque
    def maxSlidingWindow_II(self, nums, k: int):
        n = len(nums)
        if len(nums) * k == 0:
            return []
        if k == 1:
            return nums

        deq = deque()
        max_index = 0
        output = []

        # Why do we need to keep the smaller elements ?
        # Because as the window sliding through the array one by one,
        # the current maximum might change, the maximum will always be nums[deq[0]],
        # and the next maximum will always be nums[deq[1]]
        def cleanDeque(i):
            # If the current window size equals k, remove the leftmost element.
            if deq and deq[0] == i - k:
                deq.popleft()
            # Removed smaller elements which don't have any chance to become the current window maximum
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

        # Process the initial first window elements
        for i in range(k):
            cleanDeque(i)
            deq.append(i)
            if nums[i] > nums[max_index]:
                max_index = i
        output.append(nums[max_index])

        # Process the rest starting from index k
        for i in range(k, n):
            cleanDeque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

    # Dynamic Programming
    def maxSlidingWindow_III(self, nums, k: int):
        n = len(nums)
        if not n or not k or n < k: return []
        if n == k: return [max(nums)]
        if k == 1: return nums

        output = []
        left, right = [0] * n, [0] * n
        left[0] = nums[0]
        right[-1] = nums[-1]

        # Create left array
        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])

        # Create right array
        for j in range(n-2, -1, -1):
            if j % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])

        print(left)
        print(right)
        for l in range(n - k + 1):
            output.append(max(left[l + k - 1], right[l]))

        return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow_III(nums, k))
