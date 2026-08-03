import pygame


class EnergyRing:
    def __init__(self):
        self.radius = 10

    def update(self):
        self.radius += 3
        if self.radius > 400:
            self.radius = 10

    def draw(self, screen, center):
        pygame.draw.circle(screen, (255, 40, 150), center, self.radius, 2)
