# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        rooms = []
        intervals.sort(key=lambda x: x.start)
        rooms.append(intervals[0])
        # room, prevInterval = 1, intervals[0]
        for i in range(1, len(intervals)):
            for j in range(len(rooms)):
                if intervals[i].start >= rooms[j].end:
                    rooms[j], intervals[i] = intervals[i], None
                    break
            if intervals[i]:
                rooms.append(intervals[i])
        return len(rooms)

s = Solution()
i_list = [Interval(2, 11), Interval(6, 16), Interval(11, 16)]
print(s.minMeetingRooms(i_list))
