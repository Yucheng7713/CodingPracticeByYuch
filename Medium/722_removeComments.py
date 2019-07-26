class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        c_buffer, result = "", []
        skip = False
        for line in source:
            i = 0
            while i < len(line):
                c = line[i]
                # Case for "//"
                if c == "/" and i + 1 < len(line) and line[i + 1] == "/" and not skip:
                    break
                # Case for "/*"
                elif c == "/" and i + 1 < len(line) and line[i + 1] == "*" and not skip:
                    skip = True
                    i += 1
                # Case for "*/"
                elif c == "*" and i + 1 < len(line) and line[i + 1] == "/" and skip:
                    skip = False
                    i += 1
                elif not skip:
                    c_buffer += c
                i += 1
            if c_buffer and not skip:
                result.append(c_buffer)
                c_buffer = ""
        return result


