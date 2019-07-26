from statistics import median

class QuickSort:
    def __init__(self):
        self.comparedCount = 0

    def quickSort(self, start, end, list):
        # Base case : len(list) == 1
        if start >= end:
            return
        # Get the index of pivot (in the sorted array)
        split = self.partition_III(start, end, list)
        self.quickSort(start, split - 1, list)
        self.quickSort(split + 1, end, list)

    def partition_I(self, l, r, list):
        # Choose the first element as pivot
        pivot = list[l]
        # Partition phase - O(n)
        i = l + 1
        for j in range(l+1, r):
            if list[j] < pivot:
                list[i], list[j] = list[j], list[i]
                i += 1
        # Swap the chosen pivot to the right position
        list[l], list[i-1] = list[i-1], list[l]
        # Return the index of pivot
        self.comparedCount += (r - l - 1)
        return i


    def partition_II(self, l, r, list):
        # Choose the first element as pivot
        list[l], list[r-1] = list[r-1], list[l]
        pivot = list[l]
        # Partition phase - O(n)
        i = l + 1
        for j in range(l + 1, r):
            if list[j] < pivot:
                list[i], list[j] = list[j], list[i]
                i += 1
        # Swap the chosen pivot to the right position
        list[l], list[i - 1] = list[i - 1], list[l]
        # Return the index of pivot
        self.comparedCount += (r - l - 1)
        return i

    def partition_III(self, l, r, list):
        mid = (r-l+1) // 2 if (r-l+1) % 2 != 0 else (r-l+1) // 2 - 1
        mid += l
        m = median([list[l], list[mid], list[r]])
        if m == list[mid]:
            p = mid
        elif m == list[l]:
            p = l
        else:
            p = r
        if p != l:
            list[l], list[p] = list[p], list[l]
        pivot = list[l]
        # Partition phase - O(n)
        i = l + 1
        for j in range(l + 1, r + 1):
            if list[j] < pivot:
                list[i], list[j] = list[j], list[i]
                i += 1
        # Swap the chosen pivot to the right position
        list[l], list[i - 1] = list[i - 1], list[l]
        # Return the index of pivot
        self.comparedCount += (r - l)
        return i-1


class readIntoList:
    def readFromFile(self):
        txt_file = open("QuickSort.txt", "r")
        nums = txt_file.read().split('\n')
        txt_file.close()
        return [int(n) for n in nums]

# a = [3, 8, 2, 5, 1, 4, 7, 6]
a = readIntoList().readFromFile()
q = QuickSort()
q.quickSort(0, len(a)-1, a)
print(q.comparedCount)
print(a)