class Solution:
    def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':
        ans = ""
        # If one of them is negative
        if numerator * denominator < 0:
            ans += "-"
        # If there is no decimal part
        if numerator % denominator == 0:
            return str(numerator // denominator)
        numerator, denominator = abs(numerator), abs(denominator)
        ans += str(numerator // denominator)
        ans += '.'
        numerator %= denominator
        i = len(ans)
        # Use hash map to store ith digit so we can easily locate
        # the recurring digits when a repeated reminder occurs.
        f_map = dict()
        while numerator != 0:
            if numerator not in f_map:
                f_map[numerator] = i
            # Recurring division happens, return fraction
            else:
                i = f_map[numerator]
                ans = ans[:i] + '(' + ans[i:] + ')'
                return ans
            numerator *= 10
            # Append q
            ans += str(numerator // denominator)
            numerator %= denominator
            i += 1
        return ans


print(Solution().fractionToDecimal(4, 333))