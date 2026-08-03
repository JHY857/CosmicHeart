import math


class PulseTimer:
    def __init__(self):
        self.time = 0

    def update(self):
        self.time += 0.05

    def value(self):
        return (math.sin(self.time) + 1) / 2
