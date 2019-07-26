class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_32 = '{0:032b}'.format(n)[::-1]

        return int(bin_32, 2)

s = Solution()
print(s.reverseBits(43261596))