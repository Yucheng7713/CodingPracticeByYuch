class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower == upper:
                return [str(lower)]
            return [str(lower) + "->" + str(upper)]
        result = []
        if nums[0] - lower > 1:
            result += [str(lower) + "->" + str(nums[0] - 1)]
        elif nums[0] - lower == 1:
            result += [str(lower)]
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                l, r = nums[i] + 1, nums[i+1] - 1
                if l == r:
                    result += [str(l)]
                else:
                    result += [str(l) + "->" + str(r)]
        if upper - nums[-1] > 1:
            result += [str(nums[-1] + 1) + "->" + str(upper)]
        elif upper - nums[-1] == 1:
            result += [str(upper)]
        return result