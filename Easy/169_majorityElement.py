class Solution:
    def majorityElement(self, nums):
        num_count = dict()
        major = None
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
            if major == None or num_count[num] > num_count[major]:
                major = num
        return major

    def majorityElement_II(self, nums):
        nums.sort()
        return nums[len(nums) // 2]