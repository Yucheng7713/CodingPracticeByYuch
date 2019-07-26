class Solution:
    def nextClosestTime(self, time):
        t = 60 * int(time[:2]) + int(time[3:])
        validDigit = {int(digit) for digit in time if digit != ':'}
        while True:
            # Move the clock 1 min forward
            t = (t + 1) % (24 * 60)
            if all(digit in validDigit for block in divmod(t, 60) for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(t, 60))

# 02d formats an integer (d) to a field of minimum width 2 (2), with zero-padding on the left (leading 0):
# the 02d part is documented in the Format Specification Mini-Language

s = Solution()
print(s.nextClosestTime("19:34"))