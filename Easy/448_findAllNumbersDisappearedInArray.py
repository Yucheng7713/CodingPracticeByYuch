class Solution:
    # With extra space
    # Time complexity : O(n)
    # Space complexity : O(n)
    def findDisappearedNumbers(self, nums):
        d_nums = [0] * len(nums)
        for i in range(len(nums)):
            d_nums[nums[i] - 1] = 1
        return [k+1 for k in range(len(d_nums)) if d_nums[k] == 0]

    # Without extra space
    # To find the missing elements in place, one needs to find a way to track the existence of elements by marking them
    # Time complexity : O(n)
    # Space complexity : O(1) - Assume that the return list doesn't count as extra space
    def findDisappearedNumbers_II(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [k + 1 for k in range(len(nums)) if nums[k] > 0]

s = Solution()
arr = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(arr))