class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # If num contains 1, 2, 3, 4, 5, 7 -> return false
        invalid_num = ['2', '3', '4', '5', '7']
        valid_num = ['0', '1', '6', '8', '9']
        rotated_num = ""
        for i in range(len(num)-1, -1, -1):
            if num[i] in invalid_num: return False
            elif num[i] == '6':
                rotated_num += '9'
            elif num[i] == '9':
                rotated_num += '6'
            else:
                rotated_num += num[i]
        return num == rotated_num