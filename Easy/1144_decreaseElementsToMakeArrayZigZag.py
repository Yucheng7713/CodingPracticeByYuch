from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def zigZagCheck(up, nums):
            total_move = move = 0
            for i in range(len(nums) - 1):
                if up and nums[i] <= nums[i + 1]:
                    move = nums[i + 1] - nums[i] + 1
                    if nums[i + 1] - move < 0:
                        return float('inf')
                    else:
                        total_move += move
                        nums[i + 1] -= move
                elif not up and nums[i] >= nums[i + 1]:
                    move = nums[i] - nums[i + 1] + 1
                    if nums[i] - move < 0:
                        return float('inf')
                    else:
                        total_move += move
                        nums[i] -= move
                up = not up
            return total_move

        return min(zigZagCheck(False, nums[:]), zigZagCheck(True, nums[:]))

nums = [3,1,7,4,4,1,1,10,10,9]
print(Solution().movesToMakeZigzag(nums))