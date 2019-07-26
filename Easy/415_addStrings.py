class Solution:
    def addStrings(self, num1, num2):
        def strToInt(num):
            strToNum = { '0': 0, '1': 1, '2': 2, '3' : 3, '4' : 4, '5' : 5,
                       '6' : 6, '7' : 7, '8' : 8, '9' : 9}
            result = 0
            for c in num:
                result *= 10
                result += strToNum[c]
            return result
        return str(strToInt(num1) + strToInt(num2))

