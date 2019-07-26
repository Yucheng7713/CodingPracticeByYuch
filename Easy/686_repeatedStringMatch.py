class Solution:
    def repeatedStringMatch(self, A, B):
        str_time = 1
        multi_A = A
        while len(multi_A) <= 10000:
            if B in multi_A:
                return str_time
            multi_A += A
            str_time += 1
        return -1


s = Solution()
a, b = "abc", "cabcabca"
print(s.repeatedStringMatch(a, b))