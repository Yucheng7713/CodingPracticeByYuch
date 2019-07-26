class Solution:
    # String manipulation
    def validUtf8_String(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        # Convert each integer into byte format ( 8 bits ), if the number of bit > 8,
        # Get the least 8 bits as we need
        b_str = ['{0:08b}'.format(n)[-8:] for n in data]
        index = 0
        while index < len(b_str):
            # Get the number of leading 1 in the byte
            numOfBytes = len(b_str[index]) - len(b_str[index].lstrip('1'))
            # If the number of leading 1 > 5 : Invalid UTF-8
            # Since a valid UTF-8 only range from 1 ~ 4 bytes, which would only possible to have
            # 1 ~ 4 leading 1
            if numOfBytes > 4: return False
            # If the number of leading 1 is valid and won't exceed the length of the list
            if numOfBytes > 1 and numOfBytes - 1 < len(b_str):
                # Check if the following number of n - 1 bytes have leading "10"
                for i in range(1, numOfBytes):
                    # If not, it is not a valid UTF-8 character -> Return False
                    if b_str[index + i][0:2] != "10":
                        return False
                # Move the index (num of bytes - 1) as we already traverse them
                index += (numOfBytes - 1)
            # If it is a 1-byte UTF-8 : check if the leading bit is 0
            # If not, it is also not a valid UTF-8 -> Return False
            elif b_str[index][0] != "0": return False
            index += 1
        return True

    def validUtf8_bitManipulation(self, data):
        n_bytes = 0
        # mask_1 = 10000000
        mask_1 = 1 << 7
        # mask_2 = 1000000
        mask_2 = 1 << 6
        for num in data:
            # Start of a UTF-8 character -> checking its number of bytes
            if n_bytes == 0:
                mask = 1 << 7
                # Check the number of leading 1 starting from significant 8 bit ( -> 10000000 )
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1
                # If no leading 1 -> it's a valid 1-byte UTF-8
                if n_bytes == 0:
                    continue
                # If there is only 1 leading 1 or the number of bytes > 4
                # It is not a valid UTF-8 character -> return False
                elif n_bytes == 1 or n_bytes > 4:
                    return False
            # Now still checking the following n - 1 bytes if they all have leading "10"
            else:
                # If not the leading 2 bits are not "10"
                # It is not a valid UTF-8 character -> return False
                if not (num & mask_1 and not (num & mask_2)):
                    return False
            # Decrease the number of pending checking bytes
            n_bytes -= 1
        return n_bytes == 0


data_1 = [197, 130, 1]
data_2 = [235, 140, 4]
data_3 = [115,100,102,231,154,132,13,10]
data_4 = [250,145,145,145,145]
print(Solution().validUtf8_bitManipulation(data_4))