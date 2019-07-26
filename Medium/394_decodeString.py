class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for d in s:
            # push character until there is an encoded block
            if d is not "]":
                stack += [d]
            # start decoding the encounter block
            else:
                block = stack.pop()
                while stack[-1] is not "[":
                    block = stack.pop() + block
                stack.pop()
                dec, time = 1, 0
                # Calculate the number of repeated time
                while stack and stack[-1] >= '0' and stack[-1] <= '9':
                    time += int(stack.pop()) * dec
                    dec *= 10
                # Repeat the block 'time' time
                block *= time
                for b in block:
                    stack += [b]
        return "".join(stack)
