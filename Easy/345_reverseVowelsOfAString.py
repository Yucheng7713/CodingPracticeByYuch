class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        r_list = [l for l in s_list if l in vowels]
        r_str = []
        for s in s_list:
            if s in vowels:
                r_str.append(r_list.pop())
            else:
                r_str.append(s)
        return "".join(r_str)

print(Solution().reverseVowels("hello"))