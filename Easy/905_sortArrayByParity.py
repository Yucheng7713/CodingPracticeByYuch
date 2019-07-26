class Solution:
    def sortArrayByParity(self, A):
        o_list, e_list = [], []
        for num in A:
            if num % 2 == 1:
                o_list.append(num)
            else:
                e_list.append(num)
        return e_list + o_list

    def sortArrayByParity_II(self, A):
        start, end = 0, len(A) - 1
        while start < end:
            m, n = A[start], A[end]
            if m % 2 == 1 and n % 2 == 0:
                A[start], A[end] = n, m
            elif m % 2 == 1:
                end -= 1
            elif n % 2 == 0:
                start += 1
            else:
                start += 1
                end -= 1
        return A