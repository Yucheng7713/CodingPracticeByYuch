class TimeMap:
    # Note that the time is stricted to be incremental
    # So the map list will remain sorted by timestamp
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyMap: return None
        t_list = self.keyMap[key]
        # Use bisect to do the binary search searching for the insertion index
        # Since we are looking for the rightmost insertion index
        # and the stored element is tuple ( timestamp, string )
        # Beside timestamp, we need to give a sufficient big string value to make
        # sure we can locate the rightmost ( maximum ) index
        # We use '~' here which = chr(126)
        # or we can use chr(127) : delete sign instead
        index = bisect.bisect(t_list, (timestamp, ''))
        # after we have located the insertion index
        # since we need to get the previous timestamp <= timestamp
        # we look into the previous one : index - 1
        return self.keyMap[key][index - 1][1] if index else ''

        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)