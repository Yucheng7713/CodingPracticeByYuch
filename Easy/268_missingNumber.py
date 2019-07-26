class Solution:
    def missingNumber(self, nums):
        e_arr = [0] * (len(nums) + 1)
        for num in nums:
            e_arr[num] += 1

        return e_arr.index(0)

    def missingNumber_II(self, nums):
        n = len(nums)
        return int(n * (n + 1) / 2 - sum(nums))

    def missingNumber_III(self, nums):
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing


s = Solution()
n_list = [0,1]
print(s.missingNumber(n_list))