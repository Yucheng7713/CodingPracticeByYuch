class Solution(object):
    def plusOne(self, digits):
        digits[len(digits) - 1] += 1
        carry = 0
        if digits[len(digits) - 1] > 9:
            digits[len(digits) - 1] = 0
            carry = 1
            for i in range(len(digits) - 2, -1, -1):
                if digits[i] + carry > 9:
                    digits[i] = 0
                else:
                    digits[i] += carry
                    carry = 0
        if carry == 1:
            digits = [1] + digits
        return digits