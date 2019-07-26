class MovingAverage(object):

    def __init__(self, size):
        self.window = []
        self.size = size
    def next(self, val):
        if len(self.window) >= self.size:
            self.window.pop(0)
        self.window.append(val)
        return float(sum(self.window)) / len(self.window)