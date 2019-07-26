class Solution:
    def letterCombinations(self, digits):
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(digitMap[digits[0]])
        anchor = digitMap[digits[0]]
        rest = self.letterCombinations(digits[1:])
        return [a + r for a in anchor for r in rest]

    def letterCombinations_II(self, digits: str) -> List[str]:
        # Mapping from digit to possible letters according to cell phone keyboard
        letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        # Find all combinations recursively
        def allCombinations(d_str, current_comb, result):
            # End case : d_str = ""
            if not d_str:
                result += [current_comb]
                return
            # The first digit
            k = d_str[0]
            for letter in letter_map[k]:
                allCombinations(d_str[1:], current_comb + letter, result)

        if not digits: return []
        # All combinations will be stored in the result list and return
        result = []
        allCombinations(digits, "", result)
        return result
