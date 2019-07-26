import re
class Solution:
    # Stack pop and push - Low time complexity
    def calculate_I(self, s: str) -> int:
        # Get rid of spaces and split at operators (+, - , *, /)
        s = s.replace(" ", "")
        cal_list, stack = re.split("([+-/*])", s), []
        while cal_list:
            ops = cal_list.pop(0)
            if ops == "*":
                x, y = int(stack.pop(-1)), int(cal_list.pop(0))
                stack.append(x * y)
            elif ops == "/":
                x, y = int(stack.pop(-1)), int(cal_list.pop(0))
                # e.g. -13 // 4 = -4, but it should be -3
                if x * y < 0 and x % y != 0:
                    stack.append(x // y + 1)
                else:
                    stack.append(x // y)
            elif ops == "-":
                x = int(cal_list.pop(0))
                stack.append(-x)
            else:
                if ops != "+":
                    stack.append(int(ops))
        return sum(stack)

    def calculate_II(self, s: str) -> int:
        s = s.replace(" ", "")
        sign = '+'
        current_num = 0
        stack = []
        for i in range(len(s)):
            # Accumulate number with multiple digits
            if s[i].isdigit():
                current_num = 10 * current_num + int(s[i])
            # Why do we need i == len(s) - 1 ?
            # Because we need to do the last calculation for last number
            if not s[i].isdigit() or i == len(s) - 1:
                if sign == '+':
                    stack.append(current_num)
                elif sign == '-':
                    stack.append(-current_num)
                elif sign == '*':
                    stack.append(stack.pop() * current_num)
                else:
                    stack.append(int(stack.pop() / current_num))
                # Record the next operand and reset current number after it gets processed
                sign = s[i]
                current_num = 0
        return sum(stack)

    def calculate(self, s: str) -> int:
        exp = re.split('([+-/*])', s.replace(' ', ''))
        stack = []
        while exp:
            e = exp.pop(0)
            if e == '-':
                stack.append(-int(exp.pop(0)))
            elif e == '*':
                x = stack.pop()
                stack.append(x * int(exp.pop(0)))
            elif e == '/':
                x = stack.pop()
                stack.append(x // int(exp.pop(0)))
            else:
                if e != '+':
                    stack.append(int(e))
        return sum(stack)

ns = "14-3/2"
print(Solution().calculate(ns))

