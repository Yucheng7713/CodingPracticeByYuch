# Although DFS can solve such question, it is not quite suitable for DFS to out perform the other
# methods.
class Solution_DFS:
    def __init__(self):
        self.result = set()
        self.min_removal = float('inf')

    def dfs(self, origin_ex, index, current_ex, l_count, r_count, rem_count):
        # Finish the recursion and get a edited parentheses expression
        if index == len(origin_ex):
            # If it is a valid parentheses expression
            if l_count == r_count:
                if rem_count <= self.min_removal:
                    # If a new minimum is found -> discard the result so far
                    # Reset the new minimum
                    if rem_count < self.min_removal:
                        self.result = set()
                        self.min_removal = rem_count
                    self.result.add("".join(current_ex))
        # Keep recursing
        else:
            current_p = origin_ex[index]
            # If the current indexed character is other than parentheses
            # simply include it
            if current_p != '(' and current_p != ')':
                self.dfs(origin_ex, index + 1, current_ex + [current_p], l_count, r_count, rem_count)
            else:
                # Exclude the current parenthese
                self.dfs(origin_ex, index + 1, current_ex, l_count, r_count, rem_count + 1)
                # If it is an opening parenthese -> include it anyway
                if current_p == '(':
                    self.dfs(origin_ex, index + 1, current_ex + [current_p], l_count + 1, r_count, rem_count)
                # If it is an closing parenthese -> check if every closing parenthese has a corresponding opening
                # parenthese ( if it does, include it )
                elif current_p == ')' and r_count < l_count:
                    self.dfs(origin_ex, index + 1, current_ex + [current_p], l_count, r_count + 1, rem_count)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.dfs(s, 0, [], 0, 0, 0)
        return list(self.result)

class Solution_BFS:

    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                # If we ecounter more closing parentheses in advance
                if count - 1 == 0:
                    return False
                count -= 1
        return c == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s: return [""]
        result = []
        seen = set()
        seen.add(s)
        queue = [s]


p_str = "()())()"
print(Solution_DFS().removeInvalidParentheses(p_str))