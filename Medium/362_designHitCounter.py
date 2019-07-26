class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hit_count = 0
        self.hit_record = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.hit_record or self.hit_record[-1][0] != timestamp:
            self.hit_record.append([timestamp, 1])
        else:
            self.hit_record[-1][1] += 1
        self.hit_count += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.hit_record and self.hit_record[0][0] <= timestamp - 300:
            elapse_hit = self.hit_record.pop(0)
            self.hit_count -= elapse_hit[1]
        return self.hit_count

        # Your HitCounter object will be instantiated and called as such:
        # obj = HitCounter()
        # obj.hit(timestamp)
        # param_2 = obj.getHits(timestamp)