class Solution:
    def convertToTitle(self, n):
        output = ""
        while n > 26:
            n, r = divmod(n, 26)
            # like cases n = 26, 52, 78, 104... when n is a multiple of 26
            if r == 0 and n > 1:
                n -= 1
                r = 26
            output = chr(r + 64) + output
        output = chr(n + 64) + output
        return output