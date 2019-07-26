class Solution:
    def threeSumMulti(self, A: 'List[int]', target: 'int') -> 'int':
        res = 0
        m = 1000000007
        A.sort()
        for i in range(len(A) - 2):
            k = target - A[i]
            l, r = i + 1, len(A) - 1
            while l < r:
                two_sum = A[l] + A[r]
                if two_sum < k:
                    l += 1
                elif two_sum > k:
                    r -= 1
                else:
                    if A[l] != A[r]:
                        d_l = d_r = 1
                        while l < r and A[l] == A[l + 1]:
                            l += 1
                            d_l += 1
                        while l < r and A[r] == A[r - 1]:
                            r -= 1
                            d_r += 1
                        res += d_l * d_r
                        res %= m
                        l, r = l + 1, r - 1
                    else:
                        res += (r - l + 1) * (r - l) // 2
                        res %= m
                        break
        return res

A = [1,1,2,2,3,3,4,4,5,5]
target = 8
print(Solution().threeSumMulti(A, target))