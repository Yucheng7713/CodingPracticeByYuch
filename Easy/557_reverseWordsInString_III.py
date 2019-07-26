class Solution:
    def reverseWords(self, s):
        r_str = []
        words = s.split(" ")
        for w in words:
            r_str.append(w[::-1])
        return " ".join(r_str)