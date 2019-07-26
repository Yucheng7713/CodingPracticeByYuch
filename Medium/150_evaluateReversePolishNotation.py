class Solution:
    def evalRPN(self, tokens):
        operands = ["+", "-", "*", "/"]
        stack = []
        for t in tokens:
            if t in operands:
                t1, t2 = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(t2 + t1)
                elif t == "-":
                    stack.append(t2 - t1)
                elif t == "*":
                    stack.append(t2 * t1)
                else:
                    # Be careful that in Python3
                    # -6 / 132 will result in -1
                    # -10 / 3 will result in -4
                    if t2 * t1 < 0 and t2 % t1 != 0:
                        stack.append(t2 // t1 + 1)
                    else:
                        stack.append(t2 // t1)
            else:
                stack.append(int(t))
        return stack[-1]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# print(Solution().evalRPN(tokens))