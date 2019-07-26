class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return num
        num = list(num)
        L = len(num) - k
        min_num = [0] * L
        prior_min = sorted(list(set(num)))
        f_len = L
        while f_len > 0:
            # Find the index of filling minimum number
            min_index, k = 0, len(num)
            while min_index < len(prior_min):
                min_digit = prior_min[min_index]
                if min_digit in num:
                    k = num.index(min_digit)
                if len(num[k+1:]) >= f_len - 1:
                    break
                else:
                    min_index += 1
            # Fill the minimum number
            min_num[L - f_len] = min_digit
            num = num[k+1:]
            f_len -= 1
            if len(num) == 1 and f_len == 1:
                min_num[-1] = num[0]
                break
        # Get rid of leading 0
        res = "".join(min_num).lstrip("0")
        return '0' if not res else res

num = "52660469"
k = 2
print(Solution().removeKdigits(num, k))