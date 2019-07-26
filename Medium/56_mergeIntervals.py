class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    # Merge in the list with space complexity O(N)
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        i = 0
        # Important part : sort by their start
        intervals.sort(key=lambda x: x.start)
        while i < len(intervals) - 1:
            if intervals[i].end >= intervals[i+1].start and intervals[i].start <= intervals[i+1].end:
                intervals[i].start = min(intervals[i].start, intervals[i+1].start)
                intervals[i].end = max(intervals[i].end, intervals[i+1].end)
                # Concatenate over the ith element which is not needed in the output result
                intervals = intervals[:(i+1)] + intervals[i+2:]
            elif intervals[i].end >= intervals[i+1].start and intervals[i].start > intervals[i+1].end:
                intervals[i].start, intervals[i+1].start = intervals[i+1].start, intervals[i].start
                intervals[i].end, intervals[i+1].end = intervals[i+1].end, intervals[i].end
                i += 1
            else:
                i += 1
        return intervals

    def merge_II(self, intervals):
        if len(intervals) <= 1:
            return intervals
        merged_result = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if not merged_result or merged_result[-1].end < interval.start:
                merged_result.append(interval)
            else:
                merged_result[-1].end = max(merged_result[-1].end, interval.end)
        return merged_result


s = Solution()
a, b, c, d, e, f, g = Interval(2, 3), Interval(2, 2), Interval(3, 3), Interval(1, 3), Interval(5, 7), Interval(2, 2), Interval(4, 6)
i_list = [a, b, c, d, e, f, g]
i_list = s.merge(i_list)

for i in range(len(i_list)):
    print("(" + str(i_list[i].start) + "," + str(i_list[i].end) + ")")