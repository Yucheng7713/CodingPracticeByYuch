class Solution:
    def titleToNumber(self, s):
        output = 0
        p = len(s) - 1
        for c in s:
            output += pow(26, p) * (ord(c) - 64)
            p -= 1
        return output

    def titleToNumber_2(self, s):
        s = s[::-1]
        output = 0
        for exp, char in enumerate(s):
            output += 26 ** exp * (ord(char) - 64)
        return output

    def titleToNumber_3(self, s):

        return sum(26 ** exp * (ord(char) - 64) for exp, char in enumerate(s[::-1]))