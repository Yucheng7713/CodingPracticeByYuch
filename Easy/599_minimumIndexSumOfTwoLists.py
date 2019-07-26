class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        r_set = set(list1 + list2)
        map_1 = {res : i for i, res in enumerate(list1)}
        map_2 = {res : i for i, res in enumerate(list2)}
        common_res = []
        min_sum = float('inf')
        for r in r_set:
            if r in map_1 and r in map_2:
                k = map_1[r] + map_2[r]
                if min_sum > k:
                    common_res = [r]
                    min_sum = k
                elif min_sum == k:
                    common_resI += [r]
        return common_res