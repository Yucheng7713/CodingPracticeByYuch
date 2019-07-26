class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers) - 1
        pairs = []
        while start < end:
            t_sum = numbers[start] + numbers[end]
            # Reduce the search space from [start : end] to [start + 1 : end]
            # need to increase t_sum
            if t_sum < target:
                start += 1
            # Reduce the search space from [start : end] to [start : end - 1]
            # need to decrease t_sum
            elif t_sum > target:
                end -= 1
            # The match is found -> since there is only one solution, we can simply
            # return the result.
            else:
                pairs.append([start, end])
                # Skipping duplicate numbers pointed by start
                while start < end and numbers[start] == numbers[start + 1]:
                    start += 1
                # Skipping duplicate numbers pointed by end
                while start < end and numbers[end] == numbers[end - 1]:
                    end -= 1
                start, end = start + 1, end - 1

numbers = [2,7,11,15]
target = 9
print(Solution.twoSum(numbers, target))

# Concept : Take advantage of the sorted property : use two indexes : start from head and tail