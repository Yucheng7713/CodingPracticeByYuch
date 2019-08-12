class Solution(object):
    romeToInt = { "I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000 }

    # Starting from the end, so when confronting a subtracting case, there is no need to move the cursor
    # by two, just simply subtract the previous smaller roman number and keep traversing.
    def romanToInt_I(self, s):
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

    # Straight-forwarded solution
    def romanToInt_II(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                result += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2
            else:
                result += roman_map[s[i]]
                i += 1
        return result

s = Solution()
romeString = "LVIII"
print(s.romanToInt(romeString))