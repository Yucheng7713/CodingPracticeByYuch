from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Customized comparison - concatenation
        # 30 and 3: 303 < 330 -> 3 precedes 30
        # 9 and 34: 934 > 349 -> 9 precedes 34
        def cmp(x, y):
            if x + y > y + x: return 1
            elif x + y < y + x: return -1
            else: return 0
        # Convert the integer list into string list
        str_nums = list(map(str, nums))
        str_nums = sorted(str_nums, key=cmp_to_key(cmp), reverse=True)
        return "0" if str_nums[0] == "0" else "".join(str_nums)

nums = [3,30,34,5,9]
print(Solution().largestNumber(nums))