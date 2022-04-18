from typing import List

class Solution:
    # For N Sum method :
    # Parameters include start index of sublist, list, current target,
    # current sum combination, total match combination result
    def nSum(self, s_index, nums, n, target, res, results):
        # Early termination - this condition will greatly reduce the execution time
        # If target < nums[s_index] * n, then we can gurantee that there will be no solution
        # in this recursion, since for j > s_index, nums[j] > nums[s_index]
        # suppost n = 2,
        # 2 * nums[j] > 2 * nums[s_index] > target, no mater what combination we get from
        # nums[s_index + 1:], the target could never be matched ( it will always greater than
        # target ), so we could stop recursive call from this point in advance.
        # Vice versa for target > nums[-1] * n
        if len(nums) - s_index + 1 < n or target < nums[s_index] * n or target > nums[-1] * n:
            return
        if n == 2:
            # Solved 2-Sum problem with 2 pointers method
            l, r = s_index, len(nums) - 1
            while l < r:
                t_sum = nums[l] + nums[r]
                # Reduce the search space from [l:r] to [l+1:r] for increasing t_sum
                if t_sum < target:
                    l += 1
                # Reduce the search space from [l:r] to [l:r-1] for decreasing t_sum
                elif t_sum > target:
                    r -= 1
                # The sum match is found where nums[l] + nums[r] = target
                else:
                    results.append(res + [nums[l], nums[r]])
                    # Skip the duplicates for both l and r
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # Need to move one step more, since nums[l] still = nums[l + 1]
                    # nums[r] still = nums[r - 1]
                    l, r = l + 1, r - 1
        else:
            # Recursively reduce and call nSum
            for i in range(s_index, len(nums)):
                if i > s_index and nums[i - 1] == nums[i]:
                    continue
                self.nSum(i + 1, nums, n - 1, target - nums[i], res + [nums[i]], results)


    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.nSum(0, nums, 4, target, [], results)
        return results

    def fourSum_II(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(nums: List[int], target: int) -> List[List[int]]:
            list_3sum = []
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i - 1]: continue
                s_target = target - nums[i]
                l, r = i + 1, len(nums) - 1
                while l < r:
                    two_sum = nums[l] + nums[r]
                    if two_sum > s_target:
                        r -= 1
                    elif two_sum < s_target:
                        l += 1
                    else:
                        list_3sum.append([nums[i], nums[l], nums[r]])
                        previous_l, previous_r = nums[l], nums[r]
                        while l < len(nums) and previous_l == nums[l]: l += 1
                        while r >= 0 and previous_r == nums[r]: r -= 1
            return list_3sum

        nums.sort()
        list_4sum = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]: continue
            list_3sum = threeSum(nums[i + 1:], target - nums[i])
            if list_3sum:
                for l in list_3sum:
                    list_4sum.append([nums[i]] + l)
        return list_4sum


class Solution_test:
    def nSum(self, i, nums, n, target, comb, result):
        if len(nums) - i + 1 < n or target < nums[i] * n or target > nums[-1] * n:
            return
        if n == 2:
            l, r = i, len(nums) - 1
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum > target:
                    r -= 1
                elif two_sum < target:
                    l += 1
                else:
                    result.append(comb + [nums[l], nums[r]])
                    previous_l, previous_r = nums[l], nums[r]
                    while l < len(nums) and previous_l == nums[l]: l += 1
                    while r >= 0 and previous_r == nums[r]: r -= 1
        else:
            for j in range(i, len(nums)):
                if j > 0 and nums[j - 1] == nums[j]: continue
                self.nSum(j + 1, nums, n - 1, target - nums[j], comb + [nums[j]], result)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        self.nSum(0, nums, 4, target, [], result)
        return result

nums = [0,0,0,0]
print(Solution_test().fourSum(nums, 0))