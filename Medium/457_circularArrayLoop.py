class Solution:
    # Method : for each index i, check if the cycle starting at ith is valid or not
    # If it is valid -> return True
    # If it is not valid ->
    # Mark all elements in the failed cycle to 0,
    def circularArrayLoop(self, nums: 'List[int]') -> 'bool':
        # Check if there is a cycle started at ith index and whether it is valid or not
        n = len(nums)
        for i, num in enumerate(nums):
            # No move is available
            if num == 0:
                continue
            # Check if the cycle starting from ith index is valid or not
            current = i
            # Move direction : 1 -> right, -1 -> left
            dir = 1 if num > 0 else -1
            visited = set()
            # Continue until confronting an anti-direction element
            while nums[current] * dir > 0:
                # next move index
                nxt_index = (current + nums[current]) % n
                # mark as visited
                nums[current] = 0
                # record the visited index
                visited.add(current)
                # If we reach a visited index
                if nxt_index in visited and current != nxt_index:
                    return True
                current = nxt_index
        return False

print(Solution().circularArrayLoop(nums))

