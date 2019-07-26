import random
class Solution:
    def __init__(self, w):
        self.w = w
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i - 1]

    def pickIndex(self):
        l, r = 0, len(self.w) - 1
        seed = random.randint(1, self.w[-1])
        while l < r:
            mid = (l + r) // 2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid + 1
        return l