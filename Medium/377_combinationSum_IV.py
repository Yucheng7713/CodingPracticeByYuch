class Solution:
    def __init__(self):
        self.c_map = dict()
    def combinationSum4(self, nums: 'List[int]', target: 'int') -> 'int':
        if target < 0:
            return 0
        if target == 0:
            return 1
        result = 0
        for n in nums:
            if target - n in self.c_map:
                result += self.c_map[target - n]
            else:
                result += self.combinationSum4(nums, target - n)
        self.c_map[target] = result
        return result