class Solution:
    def flipAndInvertImage(self, A):
        for r_lst in A:
            r_lst.reverse()
            for i in range(len(r_lst)):
                r_lst[i] = r_lst[i] ^ 1
        return A

    def flipAndInvertImage_II(self, A):
        for i in range(len(A)):
            A[i].reverse()
            A[i] = [n ^ 1 for n in A[i]]
        return A

s = Solution()
arr = [[1,1,0],[1,0,1],[0,0,0]]
print(s.flipAndInvertImage(arr))