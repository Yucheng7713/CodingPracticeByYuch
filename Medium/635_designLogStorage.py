class LogSystem:d
    def __init__(self):
        self.log_map = []
        self.gra_scale = {
            "Year":5,
            "Month":8,
            "Day":11,
            "Hour":14,
            "Minute":17,
            "Second":20
        }
    def put(self, id: int, timestamp: str) -> None:
        self.log_map.append((id, timestamp))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        index = self.gra_scale[gra]
        start, end = s[:index], e[:index]
        # Simply compare with string directly
        return sorted([tid for tid, tmp in self.log_map if start <= tmp[:index] <= end])


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)