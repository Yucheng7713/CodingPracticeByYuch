class Solution:
    def generateParenthesis(self, n):
        results = []
        def parenthesisGenerator(p_str = []):
            if len(p_str) == 2 * n:
                if validParenthesis(p_str):
                    results.append("".join(p_str))
            else:
                p_str.append("(")
                parenthesisGenerator(p_str)
                p_str.pop()
                p_str.append(")")
                parenthesisGenerator(p_str)
                p_str.pop()

        def validParenthesis(p_str):
            balance = 0
            for p in p_str:
                if p == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        parenthesisGenerator()
        return results


s = Solution()
print(s.generateParenthesis(2))

