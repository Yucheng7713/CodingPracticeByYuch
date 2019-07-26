class CustomedSort:
    def mergeSort(self, list):
        # Merging function
        def merge(list_A, list_B):
            merged_list = []
            i = j = 0
            while i < len(list_A) and j < len(list_B):
                if list_A[i] < list_B[j]:
                    merged_list += [list_A[i]]
                    i += 1
                else:
                    merged_list += [list_B[j]]
                    j += 1
            # Merge the rest part
            if i < len(list_A):
                merged_list += list_A[i:]
            if j < len(list_B):
                merged_list += list_B[j:]
            return merged_list
        # Base case : only one number left
        if len(list) == 1:
            return list
        # Perform merge sort recursively
        # Divide the list into 2 sublists
        n = len(list) // 2
        leftSubarray = self.mergeSort(list[:n])
        rightSubarray = self.mergeSort(list[n:])
        # Return the merged result
        return merge(leftSubarray, rightSubarray)

nums = [5, 4, 1, 8, 7, 2, 6, 3, 9]
nums = [1, 4, 2, 3, 4, 5, 8, 7, 13, 6]
print(CustomedSort().mergeSort(nums))