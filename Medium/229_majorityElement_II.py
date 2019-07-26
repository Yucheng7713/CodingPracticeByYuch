# Key constraints : Time complexity : O(N), Space complexity : O(1)
# -> Run in linear time without altering the array and no extra list storing
# -> Boyer-Moore Majority Vote Algorithm
# Key concept : Remove paired elements and see what elements are left : these elements
# can have a chance to be majority -> need a second loop to confirm there number of vote

class Solution(object):
    def majorityElement(self, nums):
        # Since the definition of majority here is > floor(N/3)
        # There can only be at most 2 numbers be selected -> 2 candidates
        candidate_1 = candidate_2 = None
        # Track there vote counts
        count_1 = count_2 = 0
        if not nums:
            return nums
        for n in nums:
            if n == candidate_1:
                count_1 += 1
            elif n == candidate_2:
                count_2 += 1
            else:
                # Change the candidate if the current candidate gets no vote so far
                if count_1 == 0:
                    candidate_1, count_1 = n, 1
                elif count_2 == 0:
                    candidate_2, count_2 = n, 1
                # !!! Reduce candidates vote by 1 if none of them equal to n
                else:
                    count_1, count_2 = count_1 - 1, count_2 - 1
        threshold = len(nums) // 3
        return [n for n in (candidate_1, candidate_2) if nums.count(n) > threshold]

s = Solution()
nums = [1,1,2,3,4,4]
# print(s.majorityElement(nums))

c = Counter(nums)
c