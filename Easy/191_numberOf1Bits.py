class Solution(object):
    def hammingWeight(self, n):
        bin_str = '{0:032b}'.format(n)
        print(bin_str)
        return len([n_chr for n_chr in bin_str if n_chr == '1'])

s = Solution()
print(s.hammingWeight(11))