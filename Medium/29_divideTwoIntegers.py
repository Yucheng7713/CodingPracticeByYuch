class Solution:
    def divide(self, dividend, divisor):
        q, r = divmod(dividend, divisor)
        if dividend * divisor < 0 and r != 0:
            q += 1
        # Check if the result is in domain ( -2^31 ~ 2^31 - 1 )
        return min(max(q, - pow(2, 31)), pow(2, 31) - 1)