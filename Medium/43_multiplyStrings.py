class Solution:
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"
        return str(self.strToInt(num1) * self.strToInt(num2))

    def strToInt(self, n_str):
        result = 0
        decimal = len(n_str) - 1
        for num in n_str:
            result += (ord(num) - 48) * pow(10, decimal)
            decimal -= 1
        return result

s = Solution()
print(s.multiply("2","3"))