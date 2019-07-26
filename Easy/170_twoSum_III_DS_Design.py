class TwoSum:

    def __init__(self):
        self.sum_map = {}
    def add(self, number):
        self.sum_map[number] = self.sum_map.get(number, 0) + 1

    def find(self, value):
        for number, appears in self.sum_map.items():
            target = value - number
            if target in self.sum_map and (target != number or self.sum_map[target] > 1):
                return True
        return False