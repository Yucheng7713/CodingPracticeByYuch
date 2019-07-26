class Solution:
    # Use set() to track duplicate - bad performance
    def combinationSum3(self, k: int, n: int):
        def backTracking(k, n, combin, result):
            if k == 1:
                if n not in combin and n >= 1 and n <= 9:
                    combin.add(n)
                    combin_list = sorted(list(combin))
                    if combin_list not in result:
                        result.append(combin_list)
                    combin.remove(n)
                return
            for i in range(1, 10):
                if i not in combin:
                    combin.add(i)
                    backTracking(k - 1, n - i, combin, result)
                    combin.remove(i)
        result = []
        combin = set()
        backTracking(k, n, combin, result)
        return result

    # Use an index to avoid duplicate in [1,...,9]
    def combinationSum3_II(self, k: int, n: int):
        def backTracking(k, n, index, combin, result):
            if k < 0 or n < 0:
                return
            if k == 0 and n == 0:
                result.append(combin)
                return
            for i in range(index, 10):
                backTracking(k - 1, n - i, i + 1, combin + [i], result)

        result = []
        backTracking(k, n, 1, [], result)
        return result
k = 4
n = 24
print(Solution().combinationSum3(k, n))