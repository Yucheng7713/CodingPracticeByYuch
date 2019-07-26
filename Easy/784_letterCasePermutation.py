class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def casePermute(current_s, s, paths):
            if not s:
                paths.append(current_s)
                return
            l, rest = s[0], s[1:]
            if l.isalpha():
                lower_l = chr(ord(l) - 32) if 97 <= ord(l) <= 122 else l
                upper_l = chr(ord(l) + 32) if 65 <= ord(l) <= 90 else l
                casePermute(current_s + lower_l, rest, paths)
                casePermute(current_s + upper_l, rest, paths)
            else:
                casePermute(current_s + l, rest, paths)

        results = []
        casePermute('', S, results)
        return results