class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ver_1, ver_2 = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                ver_1[i] = nums[i+1]
                ver_2[i+1] = nums[i]
                break
        return all(ver_1[i] <= ver_1[i+1] for i in range(len(ver_1)-1)) or all(ver_2[i] <= ver_2[i+1] for i in range(len(ver_2)-1))

    # With valid comparison, e.g. 3, 4, 2, 3
    def checkPossibility_II(self, nums: List[int]) -> bool:
        modify = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if modify or (i > 0 and nums[i - 1] > nums[i + 1]) and (i + 2 < len(nums) and nums[i + 2] < nums[i]):
                    return False
                modify = True
        return True