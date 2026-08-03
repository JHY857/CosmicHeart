import math


class Camera:
    def __init__(self):
        self.zoom = 1.0

    def update(self, t):
        self.zoom = 1 + math.sin(t) * 0.03

    def transform(self, x, y, cx, cy):
        return ((x-cx)*self.zoom+cx, (y-cy)*self.zoom+cy)
