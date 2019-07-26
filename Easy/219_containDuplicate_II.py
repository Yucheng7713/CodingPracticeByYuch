class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if nums == []:
            return False
        c_map = dict()
        for i, v in enumerate(nums):
            if v not in c_map.keys():
                c_map[v] = i
            else:
                c_map[v] = i - c_map.get(v)
                if c_map[v] <= k:
                    return True
        return False

    def containsNearbyDuplicate_II(self, nums, k):
        if nums == []:
            return False
        c_map = dict()
        for i, v in enumerate(nums):
            if v in c_map and i - c_map.get(v) <= k:
                return True
            c_map[v] = i
        return False

s = Solution()
arr_1 = [1,2,3,1]
arr_2 = [1,2,3,1,2,3]
arr_3 = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
arr_4 = [1,0,1,1]
arr_5 = []
print(s.containsNearbyDuplicate(arr_5, 1))