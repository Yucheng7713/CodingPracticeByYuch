import collections

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0
        pairs_map = collections.defaultdict(int)
        time = [n % 60 for n in time]
        for t in time:
            # Try to make each t range from 0 ~ 59, even for (60 - t)
            # otherwise in case t = 0, 60 - t = 60, which is not what we are looking for.
            pairs += pairs_map[(60 - t) % 60]
            pairs_map[t] += 1
        return pairs

times = [60,60,60]
print(Solution().numPairsDivisibleBy60(times))