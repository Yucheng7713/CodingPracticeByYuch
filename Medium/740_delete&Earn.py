import collections

class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Make the number in the list unique -> keep each number only once
        n_list = list(set(nums))
        n_list.sort()
        # points list : the number of time occur
        points, earn_points = collections.Counter(nums), [0, 0]
        # calculate the earned points when picking number n
        for n in n_list:
            earn_points += [n * points[n]]
        curr_earn, prev_earn = 1, 0
        for i in range(2, len(earn_points)):
            # If the current observed number is adjacent to previous number
            # Need to decide whether or not to pick the number by comparing
            # previous earn points
            if i > 2 and n_list[i-2] - n_list[i-3] == 1:
                earn_points[i] = max(earn_points[i] + earn_points[prev_earn], earn_points[curr_earn])
            # If not then we can pick it without any concern
            else:
                earn_points[i] += earn_points[curr_earn]
            prev_earn, curr_earn = prev_earn + 1, curr_earn + 1
        return earn_points[-1]

ns = [2, 2, 3, 3, 3, 4]
print(Solution().deleteAndEarn(ns))

