class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            num = x
            reverse_num = 0
            while num > 0:
                reverse_num *= 10
                reverse_num += (num % 10)
                num /= 10
            if x == reverse_num:
                return True
        return False