class Solution(object):
    def addBinary(self, a, b):
        a_index, b_index = len(a) - 1, len(b) - 1
        sum = carry = 0
        a_binary = b_binary = r_binary = ""
        while a_index > -1 or b_index > -1 or carry:
            if a_index > -1:
                a_binary = a[a_index]
                a_index -= 1
            else:
                a_binary = "0"
            if b_index > -1:
                b_binary = b[b_index]
                b_index -= 1
            else:
                b_binary = "0"
            carry, sum = divmod(int(a_binary) + int(b_binary) + carry, 2)
            r_binary = str(sum) + r_binary
        return r_binary

s = Solution()
print(s.addBinary("11","1"))