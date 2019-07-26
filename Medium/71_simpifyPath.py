import re

class Solution:
    def simplifyPath(self, path: 'str') -> 'str':
        paths = path.split('/')
        simp_path = []
        for dirt in paths:
            if simp_path and dirt == "..":
                simp_path.pop()
            elif dirt and (dirt != ".." and dirt != "."):
                simp_path.append(dirt)
        return "/" if not simp_path else "/".join([""] + simp_path)

print(Solution().simplifyPath("/..."))