class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backTracking(current, k, n, combin, result):
            if k == 0:
                result += [combin]
            for i in range(current + 1, n + 1):
                backTracking(i, k - 1, n, combin + [i], result)
        result = []
        for i in range(1, n + 1):
            backTracking(i, k - 1, n, [i], result)
        return result