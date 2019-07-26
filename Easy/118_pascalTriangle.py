class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        output = [[1], [1, 1]]
        temp = []
        for i in range(2, numRows):
            temp.append(1)
            for j in range(i - 1):
                temp.append(output[i - 1][j] + output[i - 1][j + 1])
            temp.append(1)
            output.append(temp)
            temp = []
        return output

    # More efficient way by shifting a row in two directions then sum them up
    def generate_II(self, numRows):
        if numRows == 0:
            return []
        output = [[1]]
        for i in range(1, numRows):
            output += [list(map(lambda x, y: x + y, output[-1] + [0], [0] + output[-1]))]
        return output


s = Solution()
print(s.generate_II(5))