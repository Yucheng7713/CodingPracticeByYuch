import collections

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_map = collections.defaultdict(list)
        for i, j in trust:
            trust_map[j].append(i)
        for trusted, trustees in trust_map.items():
            if len(trustees) == N - 1 and trusted not in trustees:
                return trusted
        return -1

n = 3
trusts = [[1,3],[2,3],[3,1]]
print(Solution().findJudge(n, trusts))