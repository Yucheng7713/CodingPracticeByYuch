class Solution:
    def reverseWords(self, str: List[str]) -> None:
        """
        Do not return anything, modify str in-place instead.
        """
        j = 0
        for i in range(len(str)):
            if str[i] == " ":
                str[j:i] = str[j:i][::-1]
                j = i + 1
        str[j:] = str[j:][::-1]
        str.reverse()