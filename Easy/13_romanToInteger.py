class Solution(object):
    romeToInt = { "I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000 }
    def romanToInt(self, s):
        L = list(s)
        prevRome = L[len(L) - 1]
        integer = self.romeToInt[prevRome]
        for i in range(len(L) - 2, -1, -1):
            if self.romeToInt[L[i]] < self.romeToInt[prevRome]:
                integer -= self.romeToInt[L[i]]
            else:
                integer += self.romeToInt[L[i]]
            prevRome = L[i]
        return integer

s = Solution()
romeString = "LVIII"
print(s.romanToInt(romeString))