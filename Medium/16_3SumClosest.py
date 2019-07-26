class Solution:
    def threeSumClosest(self, nums, target):
        N = len(nums)
        # Presort the list
        nums.sort()
        # Use an additional parameter 'min_diff' to track the minimum difference
        closest_sum, min_diff = 0, float('inf')
        for i in range(N - 2):
            start, end = i + 1, N - 1
            # The difference between target and two sum result
            t = target - nums[i]
            # Get the closest two sum result to the target
            while start < end:
                t_sum = nums[start] + nums[end]
                # t - t_sum = target - nums[i] - nums[start] - nums[end]
                if abs(t - t_sum) < min_diff:
                    # min(target - nums[i] - nums[start] - nums[end])
                    min_diff = abs(t - t_sum)
                    # Record the sum of current minimum result
                    closest_sum = nums[i] + t_sum
                # Reduce the search space from [start:end] to [start+1:end]
                if t_sum < t:
                    start += 1
                # Reduce the search space from [start:end] to [start:end-1]
                elif t_sum > t:
                    end -= 1
                # The perfect match is found -> return it directly
                else:
                    return target
        return closest_sum