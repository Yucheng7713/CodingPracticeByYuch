import collections

class Solution:
    # Brute Force + Prefix Sum : TLE - Time Limited Exceed
    def subarraysDivByK(self, A, K) -> int:
        sum_list = []
        result = []
        k_sum, N = 0, len(A)
        # Form the prefix sum array
        for n in A:
            k_sum += n
            sum_list += [k_sum]
        # Iterate through all possible subarray sum
        for i in range(N):
            if sum_list[i] % K == 0:
                result.append(A[:i + 1])
            for j in range(i+1, N):
                if (sum_list[j] - sum_list[i]) % K == 0:
                    result.append(A[i + 1:j + 1])
        return len(result)

    def subarraysDivByK_II(self, A, K):
        mod = [0] * K
        current_sum, mod[0] = 0, 1
        for num in A:
            current_sum += num
            mod[current_sum % K] += 1
        return sum([v * (v - 1)/2 for v in mod])


a = [4,5,0,-2,-3,1]
k = 5
print(Solution().subarraysDivByK_II(a, k))