class Solution(object):
    def reverse(self, x):
        num = abs(x)
        reverse_num = 0
        while num > 0:
            reverse_num *= 10
            reverse_num += (num % 10)
            num /= 10
        if x < 0:
            reverse_num *= -1
        if reverse_num < 2**31 - 1 and reverse_num > -2**31:
            return reverse_num
        else:
            return 0