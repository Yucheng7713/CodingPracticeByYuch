class Solution:
    def threeSum(self, nums):
        # Presort the list in ascending order
        nums.sort()
        N = len(nums)
        triplets = []
        # Find all triplets which include nums[i]
        for i in range(N - 2):
            # Skip the replicated nums[i]
            # For example : [-4, -1, -1, 0, 1, 2], when i = 2, nums[2] = -1
            # Since we have already explored with nums[i-1] = nums[1] = -1, we skip for i = 2
            # For avoiding i - 1 < 0 case, put i > 0 as pre-condition
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Find the target number with 2 sum approach in [i+1:N] sublist
            # nums[i] + target = nums[i] + (nums[j] + nums[k]) = 0
            # target = - nums[i] = nums[j] + nums[k] -> Find nums[i] and nums[k] without duplicates
            target = -nums[i]
            # Since the array is sorted, we can use two pointers method here
            start, end = i + 1, N - 1
            while start < end:
                subsum = nums[start] + nums[end]
                # Reduce the search space from [start:end] to [start:end - 1]
                # need to reduce subsum
                if target < subsum:
                    end -= 1
                # Reduce the search space from [start:end] to [start + 1:end]
                # need to increase subsum
                elif target > subsum:
                    start += 1
                # A 2 sum match is found : record it and avoid duplicates by moving
                # both start and end index if start == start + 1 and end == end - 1
                else:
                    triplets.append([nums[i], nums[start], nums[end]])
                    # Check if the next start is the same number, if it is, move the start index
                    # to skip a stream of same numbers
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    # Check if the next start is the same number, if it is, move the start index
                    # to skip a stream of same numbers
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start, end = start + 1, end - 1
        return triplets

s = Solution()

nums = [-2, 0, 1, 1, 2]
print(s.threeSum(nums))