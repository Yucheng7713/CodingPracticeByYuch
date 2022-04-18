class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = ""
        for c in S:
            if stack and stack[-1] == c:
                stack = stack[:-1]
            else:
                stack += c
        return stack

s = "abbaca"
print(Solution().removeDuplicates(s))