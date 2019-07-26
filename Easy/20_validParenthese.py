class Solution(object):
    parMap = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    def isValid(self, s):
        p_elements = list(s)
        p_stack = []
        for i in range(0, len(p_elements)):
            if p_elements[i] in self.parMap.keys():
                p_stack.append(p_elements[i])
            elif p_elements[i] in self.parMap.values():
                if p_stack == [] or self.parMap[p_stack.pop()] != p_elements[i]:
                    return False
        return p_stack == []

s = Solution()
print(s.isValid("()"))

# class Solution_2(object):
#     parMap = {
#         "(" : 1,
#         ")" : -1,
#         "[" : 2,
#         "]" : -2,
#         "{" : 3,
#         "}" : -3
#     }
#
#     def isValid_2(self, s):
#         p_elements = list(s)
#         if p_elements != []:
#             p_stack = [p_elements[0]]
#             for i in range(1, len(p_elements)):
#                 if p_stack[-1:] != []:
#                     if self.parMap[p_stack[-1]] + self.parMap[p_elements[i]] == 0:
#                         p_stack.pop()
#                     else:
#                         p_stack.append(p_elements[i])
#                 else:
#                     p_stack.append(p_elements[i])
#         else:
#             return True;
#         return p_stack == []
#
# s2 = Solution_2()
# print(s2.isValid_2("()[]{}"))
