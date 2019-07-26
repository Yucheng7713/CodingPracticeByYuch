class Solution:
    def rotatedDigits(self, N: int) -> int:
        result = 0
        rotate_map = {
            '0':'0',
            '1':'1',
            '2':'5',
            '3':None,
            '4':None,
            '5':'2',
            '6':'9',
            '7':None,
            '8':'8',
            '9':'6'
        }
        for i in range(1, N+1):
            str_num = str(i)
            if '3' in str_num or '4' in str_num or '7' in str_num: continue
            rotated_num = "".join([rotate_map[n] for n in list(str_num)])
            if str_num != rotated_num:
                result += 1
        return result

    # Doesn't need to really rotate the number
    # As long as the number contains 2, 5, 6, 9, the result will be a good number
    # If the number contains 3, 4, 7, the result won't be a good number regardless other digits
    # If the number contains only 0, 1, 8, the result won't be a good number too
    def rotatedDigits_II(self, N: int) -> int:
        result = 0
        for i in range(1, N + 1):
            str_num = str(i)
            if '3' in str_num or '4' in str_num or '7' in str_num:
                continue
            if '2' in str_num or '5' in str_num or '6' in str_num or '9' in str_num:
                result += 1
        return result
