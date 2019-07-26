# Root digit
class Solution:
    def addDigits(self, num):
        if num == 0:
            return num
        return (num - 1) % 9 + 1