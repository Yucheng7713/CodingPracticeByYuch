class countInversion:
    def mergeCount(self, lst_a, lst_b):
        i = j = 0
        merged_lst = []
        numOfInv = 0
        while i < len(lst_a) or j < len(lst_b):
            if i < len(lst_a) and (j == len(lst_b) or lst_a[i] < lst_b[j]):
                merged_lst += [lst_a[i]]
                i += 1
            else:
                merged_lst += [lst_b[j]]
                j += 1
                numOfInv += (len(lst_a) - i)
        return numOfInv, merged_lst

    def numOfInversion(self, nums):
        n = len(nums)
        if n == 0:
            return
        if n == 1:
            return 0, nums
        x, B = self.numOfInversion(nums[:n // 2])
        y, C = self.numOfInversion(nums[n // 2:])
        z, D = self.mergeCount(B, C)
        return x + y + z, D

class readIntoList:
    def readFromFile(self):
        txt_file = open("integer.txt", "r")
        nums = txt_file.read().split('\n')
        txt_file.close()
        return [int(n) for n in nums]
nums = readIntoList().readFromFile()
print(countInversion().numOfInversion(nums))