class Solution:
    def fizzBuzz(self, n):
        nums = []
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0:
                s = ""
                if i % 3 == 0:
                    s = "Fizz"
                if i % 5 == 0:
                    s += "Buzz"
                nums.append(s)
            else:
                nums.append(str(i))
        return nums

s = Solution()
print(s.fizzBuzz(15))