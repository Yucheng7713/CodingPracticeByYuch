class Solution:
    # Check upon the length of strings with different validations
    def insertEdit(self, s, t):
        edited_str = []
        for i in range(len(t)):
            edited_str += [t[:i] + t[i + 1:]]
        return s in edited_str

    def deleteEdit(self, s, t):
        edited_str = []
        for i in range(len(s)):
            edited_str += [s[:i] + s[i + 1:]]
        return t in edited_str

    def replaceEdit(self, s, t):
        edited_str = []
        for i in range(len(s)):
            edited_str += [s[:i] + '_' + s[i + 1:]]
        for j in range(len(t)):
            r_str = t[:j] + '_' + t[j + 1:]
            if r_str in edited_str:
                return True
        return False

    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t or abs(len(s) - len(t)) > 1: return False
        if len(s) < len(t):
            return self.insertEdit(s, t)
        if len(s) > len(t):
            return self.deleteEdit(s, t)
        return self.replaceEdit(s, t)

    def isOneEditDistance_II(self, s: str, t: str) -> bool:
        # If s is t or the lengths between them is differ too much
        # there is no way they can be differ by 1 edit distance
        if s == t or abs(len(s) - len(t)) > 1: return False
        # Always assume that s is shorter than t
        # If s is longer than t, swap them
        if len(s) > len(t):
            s, t = t, s
        for i in range(len(s)):
            if s[i] != t[i]:
                # Check if the rest part is equal or not ( replace )
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                # Check if the edited part is equal or not ( deletion )
                else:
                    return s[i:] == t[i + 1:]
        # until len(s) s == t, since s is ensured to be shorter than t
        # here we can assure that t is one edit distance from s ( insertion )
        return True

