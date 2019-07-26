class Solution:
    def singleNumber(self, nums):
        n_map = dict()
        for num in nums:
            n_map[num] = n_map.get(num, 0) + 1
        for k, v in n_map.items():
            if v == 1:
                return k

    def singleNumber_II(self, nums):
        single_num = 0
        for num in nums:
            single_num ^= num
        return single_num