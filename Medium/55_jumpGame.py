class Solution(object):
    # Top-Down DP -> it works but inefficient
    def canJump(self, nums):
        e_list = [False] * (len(nums))
        e_list[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            # if it can reach to the end directly
            if (i + nums[i]) >= len(nums) - 1:
                e_list[i] = True
            else:
            # it cannot reach to the end but can reach out to a good index
            # which would eventually lead to the end
                for j in range(i + 1, len(nums) - 1):
                    if (i + nums[i]) >= j and e_list[j]:
                        e_list[i] = True
                        break
        return e_list[0]

    # Use Greedy to solve
    def canJump_II(self, nums):
        jumps = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i]) >= jumps:
                jumps = i
        return jumps == 0

s = Solution()
my_arr = [2,3,1,1,4]
my_arr_no = [2,4,2,1,0,2,0]
# print(s.canJump(my_arr))
n = 5
print(n | 1)