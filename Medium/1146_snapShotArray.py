import collections

# Memory Exceed
class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot_array = [0] * length
        self.snap_count = 0
        self.snapshot_table = collections.defaultdict(dict)

    def set(self, index: int, val: int) -> None:
        if 0 <= index < len(self.snapshot_array):
            self.snapshot_array[index] = val

    def snap(self) -> int:
        snap_id = self.snap_count
        for i, n in enumerate(self.snapshot_array):
            self.snapshot_table[snap_id][i] = n
        self.snap_count += 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot_table[snap_id][index]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)