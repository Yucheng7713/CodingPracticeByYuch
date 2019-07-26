class Solution:
    def myAtoi(self, s):
        sign = 1
        # Get rid of leading blank
        s = s.strip()
        if len(s) == 0:
            return 0
        lst = list(s)
        if lst[0] == '-':
            sign *= -1
            lst.pop(0)
        elif lst[0] == '+':
            lst.pop(0)
        result = index = 0
        while index < len(lst) and lst[index].isdigit():
            result = result * 10 + (ord(lst[index]) - ord('0'))
            index += 1
        return max(min(result * sign, pow(2, 31) - 1), -1 * pow(2, 31))