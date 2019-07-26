class Solution:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        def getKthPermutation(nums: 'List[int]', k: 'int') -> 'str':
            if k == 1:
                return "".join([str(n) for n in nums])
            if len(nums) < 3:
                if len(nums) == 0:
                    return ""
                elif len(nums) == 1:
                    return nums[0]
                else:
                    if k % 2 == 0:
                        return str(nums[1]) + str(nums[0])
                    else:
                        return str(nums[0]) + str(nums[1])
            p_count, p_num = len(nums) - 1, 1
            while p_count > 0:
                p_num *= p_count
                p_count -= 1
            head, next_head = divmod(k, p_num)
            if next_head == 0:
                head -= 1
                next_head = p_num
            return str(nums[head]) + getKthPermutation(nums[:head] + nums[head + 1:], next_head)
        nums = [i for i in range(1, n + 1)]
        return getKthPermutation(nums, k)

print(Solution().getPermutation(4, 6))
