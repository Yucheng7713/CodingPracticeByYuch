class Solution:
    def findMinDifference(self, timePoints):
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        minPoints = list(map(convert, timePoints))
        minPoints.sort()
        minPoints += [minPoints[0] + 24 * 60]
        minDiff = float('inf')
        for i in range(len(minPoints) - 1):
            minDiff = min(minDiff, minPoints[i + 1] - minPoints[i])

times = ["23:59","00:00"]
print(Solution().findMinDifference(times))