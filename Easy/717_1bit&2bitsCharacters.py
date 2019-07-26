class Solution(object):
        def isOneBitCharacter(self, bits):
            if not bits:
                return False
            b_index = 0
            while b_index < len(bits):
                if b_index == len(bits) - 1:
                    return True
                if bits[b_index] == 1:
                    b_index += 2
                else:
                    b_index += 1
            return False

        def isOneBitCharacter_II(self, bits):
            if bits == []:
                return False
            elif all(b == 0 for b in bits):
                return True
            else:
                bits = bits[::-1]
                if bits[0] == 0:
                    if bits[1] == 0:
                        return True
                    else:
                        b_index, count = 1, 0
                        while b_index < len(bits) and bits[b_index] == 1:
                            count += 1
                            b_index += 1
                        if count % 2 == 0:
                            return True
                return False

# Characters > 10, 11, 0
s = Solution()
b_str_1 = [1,0,0]
b_str_2 = [1,1,1,1,0]
print(s.isOneBitCharacter_II(b_str_2))