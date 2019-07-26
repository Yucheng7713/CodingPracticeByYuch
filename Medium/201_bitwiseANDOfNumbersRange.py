class Solution:
    # Iterative and : TLE
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n: return m
        if m == 0 or n == 0: return 0
        ans = m
        for i in range(m + 1, n + 1):
            ans = ans & i
        return ans
    # In fact it is unnecessary to bitwise all the numbers in the range,
    # just need to find the special numbers which dominates the bitwise AND result
    # There are two special numbers
    # e.g. [m = 0bxyz0acd, n=0bxyz1rst]
    # m' = 0bxyz0111, n' = 0bxyz1000
    # rangeBitwiseAnd(m, n) = m' & n' = 0bxyz0000
    def rangeBitwiseAnd_II(self, m: int, n: int) -> int:
        i = 0
        # Right shift both m and n until we get the same digit section
        # which will be the remains part after bitwise AND
        while m != n:
            m >>= 1
            n >>= 1
            # Store the number of padding digit 0
            i += 1
        return n << i

# print(Solution().rangeBitwiseAnd_II(5, 7))
print(6 >> 1)