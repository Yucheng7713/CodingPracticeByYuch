class Solution:
    def largestDivisibleSubset(self, nums: 'List[int]') -> 'List[int]':
        count = [0] * len(nums)
        parent = [0] * len(nums)
        nums.sort()
        max_n, index = 0, -1
        for i in range(len(nums)):
            # count[i] : store the size of divisible subset ending with nums[i]
            count[i] = 1
            # store the linked index for reconstructing the largest divisible subset
            parent[i] = -1
            # Find the divisors in previous of ith element
            for j in range(i-1, -1, -1):
                # If a divisor is found
                if nums[i] % nums[j] == 0:
                    # Find the maximum size of divisible subset
                    if 1 + count[j] > count[i]:
                        count[i] = count[j] + 1
                        parent[i] = j
            # Update the index of the maximum size of divisible subset
            if count[i] > max_n:
                max_n = count[i]
                index = i
        # Start from the end index of the largest divisible subset
        # Follow the linked indice stored in parent to reconstruct
        # the largest divisible subset
        res = []
        while index != -1:
            res = [nums[index]] + res
            index = parent[index]
        return res

nums = [1, 2, 3]
print(Solution().largestDivisibleSubset(nums))