class ConvertToLowerCase:
    def toLowerCase_I(self, str):

        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)

    def toLowerCase_II(self, str):

        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)

    def toLowerCase_III(selfs, str):

        return str.lower()


# class ConvertToUpperCase:
#     def toUpperCase(self, str):
#
#         return "".join(chr(ord(c) - 32) if "a" <= c <= "z" else c for c in str)
